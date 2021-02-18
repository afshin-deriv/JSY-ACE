#!/usr/bin/env python3
from scapy.all import *
import threading
import argparse
import signal
import sys
import time

def get_argument():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--interface', help = 'The interface that detector listen on it, default is loopback')
  parser.add_argument('-p', '--ssh-port', help = 'SSH port, default is 22')
  return parser.parse_args()

def signal_handler(sig, frame):
    print('Exit gracefully')
    sys.exit(0)


def parse_ssh(packet):
  if packet.haslayer(TCP):
    mac_of_ssh = getmacbyip(packet[IP].src)
    print(mac_of_ssh)


def sniff_ssh():
  sniff(iface=LOCAL_INTERFACE, filter="tcp and dst port {0}".format(SSH_PORT), prn=parse_ssh)


if __name__ == "__main__":
  args = get_argument()
  SSH_PORT           = args.ssh_port or "22"
  LOCAL_INTERFACE    = args.interface or  get_if_list()[0]
  signal.signal(signal.SIGINT, signal_handler)
  thread_parser_ssh = threading.Thread(target=sniff_ssh, args=())

  thread_parser_ssh.start()

