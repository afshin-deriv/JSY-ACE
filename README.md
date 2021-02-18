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
1. submit_flag
  #### Description
  Simple python script to submit list of stolen flags in the CTF game to the Team Interface 
  #### Usage
  ```
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
  ['alreadysubmitted:correct']
  ['alreadysubmitted:incorrect']
  ['alreadysubmitted:correct']
  ['alreadysubmitted:incorrect']
  ['alreadysubmitted:correct']
  ['alreadysubmitted:incorrect']
  ['alreadysubmitted:correct']
  ['alreadysubmitted:incorrect']
  ['alreadysubmitted:correct']
  ['alreadysubmitted:incorrect']
  ['alreadysubmitted:incorrect']
  ```
