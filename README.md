# Team *JSY-ACE*
CSE545 - Software Security - ASU Spring 2021

Members:
1. Chao Wan, cwan13@asu.edu
2. Edy Widjaja, ewidjaja@asu.edu
3. Jie Jin, jjin19@asu.edu
4. Santoso Ham, sham8@asu.edu
5. Yan Xue, yxue36@asu.edu
6. Afshin Paydar, apaydar@asu.edu

## Our Tools
## 1. submit_flag
  #### Description
  Simple python script to submit list of stolen flags from file to the Team Interface in the CTF game.
  the input file must contains a flag in each line.  
  #### Usage
  ```
  $ git clone git@github.com:afshinpaydar-binary/JSY-ACE.git
  $ cd JSY-ACE/Submit_Flags
  $ make
  $ bin/submit_flag -h
    Usage: submit_flag [options]

    Options:
    -h, --help            show this help message and exit
    -i TEAM_INTERFACE, --team-interface=TEAM_INTERFACE
                        Team interface on CTF game
    -t FLAG_TOKEN, --flag-token=FLAG_TOKEN
                        Flag token
    -f STOLEN_FLAGS, --stolen-flags=STOLEN_FLAGS
                        File of stolen flags, a flag in each line

  $ ./bin/submit_flag -i 52.52.83.248 -t pc9Zhk3DDDV9Y5ILrUs2 -f flags.txt
  ```
  #### Sample Output
  ```
  $ ./bin/submit_flag -i 52.52.83.248 -t pc9Zhk3DDDV9Y5ILrUs2 -f flags.txt
  ['correct']
  ['alreadysubmitted:incorrect']
  ['alreadysubmitted:correct']
  ```
  #### Clean UP
  ```
  $ make clean
  ```
  ![Redirector](images/Redirector.png?raw=true "Redirector diagram")
  ## 2. Redirector
  #### Description
  The goal of this tool is to hide our IP address behind one of top teams(at chart) in the CTF game, by redirection of all traffic 
  with destination to specific ports to another team and from source of our second IP address, then reply to the attacker with return traffic
  So we can survive behind others patch and have more time to patch our services.
  In order to use this tools, it needed to DROP the return traffice from our IP by iptables rules.

  #### Usage
  ```
  $ git clone git@github.com:afshinpaydar-binary/JSY-ACE.git
  $ cd JSY-ACE/Redirector
  $ make
  $ bin/redirector -h
    usage: redirector [-h] [-i TUN_INTERFACE] [-o REAL_INTERFACE] [-H HIDE_IP] [-v VICTIM_IP] [-r REDIRECTOR_IP] [-e REDIRECTOR_ETHERNET] [-m MASQUERADE_IP] [-p PORTS]

    optional arguments:
      -h, --help            show this help message and exit
      -i TUN_INTERFACE, --tun-interface TUN_INTERFACE
                            The tunnel interface
      -o REAL_INTERFACE, --real-interface REAL_INTERFACE
                            The physical interface
      -H HIDE_IP, --hide-ip HIDE_IP
                            Our IP address that will hide behind Victim address
      -v VICTIM_IP, --victim-ip VICTIM_IP
                            Destination victim IP address that traffic route to that
      -r REDIRECTOR_IP, --redirector-ip REDIRECTOR_IP
                            Intermediary IP address for redirection usage
      -e REDIRECTOR_ETHERNET, --redirector-ethernet REDIRECTOR_ETHERNET
                            Intermediary MAC address for redirection usage
      -m MASQUERADE_IP, --masquerade-ip MASQUERADE_IP
                            Masquerade IP address in the CTF game
      -p PORTS, --ports PORTS
                            List comma seperated local ports that will hide by redirect traffic to victim (e.g: 10001, 20001)  
  
  $ tmux
  $ ./bin/redirector -i tun0 -o eth0 -H 10.9.3.3 -v 10.9.3.4 -r 172.16.20.3 -e 5e:28:70:8a:b:c6 -m 10.9.3.1 -p 10001,10002,10003,10004
  ```
  ## 3. exploit_runner.py
  #### Description
  
  #### Usage
  ```
  $ python3 exploit_runner.py -e backup_exploit_1-11
  $ python3 exploit_runner.py -e backup_exploit_12-25
  $ python3 exploit_runner.py -e backup_exploit_26-39
  #### Clean UP
  ```
  $ make clean
  ```
