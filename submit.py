#!/usr/bin/python
import sys
import swpag_client

print("Welcome!")
t = swpag_client.Team('http://13.56.188.54', 'pc9Zhk3DDDV9Y5ILrUs2')
flag = input("Input flag: ")
print(t.submit_flag(['%s']), flag)
# print("Submit flag: %s", str(sys.argv[1]))
