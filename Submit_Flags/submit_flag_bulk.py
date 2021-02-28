#!/usr/bin/env python3

import swpag_client
import optparse

def get_argument():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--team-interface", dest="team_interface", help = 'Team interface on CTF game')
  parser.add_option("-t", "--flag-token", dest="flag_token", help = 'Flag token')
  parser.add_option("-f", "--stolen-flags", dest="stolen_flags", help = 'File of stolen flags, a flag in each line')

  (options, arguments) = parser.parse_args()
  if not options.team_interface:
    parser.error("[-] Please specify Team interface, use --help for more info.")
  elif not options.flag_token:
    parser.error("[-] Please specify Flag Token, use --help for more info.")
  elif not options.stolen_flags:
    parser.error("[-] Please specify a file contains list of flags to submit, use --help for more info.")
  return options

if __name__ == "__main__":
  options = get_argument()
  ctf_game = swpag_client.Team("http://"+options.team_interface, options.flag_token)
  flags_file = open(options.stolen_flags, 'r')
  flag_lines = flags_file.readlines()

  for flag in flag_lines:
    print(ctf_game.submit_flag(["{}".format(flag.strip())]))

