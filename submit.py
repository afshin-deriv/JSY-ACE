#!/usr/bin/python
import sys
import swpag_client

print("Welcome!")
t = swpag_client.Team('http://52.52.83.248', 'pc9Zhk3DDDV9Y5ILrUs2')
flag = input("Input flag: ")
print(t.submit_flag(['%s']), flag)
# print("Submit flag: %s", str(sys.argv[1]))
