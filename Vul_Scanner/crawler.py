#!/usr/bin/env python3

from scapy.all import *
import threading
import optparse
import signal
import sys
import time

def get_argument():
  parser = optparse.OptionParser()
  parser.add_option("-u", "--url", dest="url", help = 'Destination URL for scan')
  (options, arguments) = parser.parse_args()
  if not options.url:
    parser.error("[-] Please specify a destination URL, use --help for more info.")
  return options


if __name__ == "__main__":
  options = get_argument()
