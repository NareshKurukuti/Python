import json

username = input("please enter your username")
filename = 'username.json'
"""Example of Write"""
with open(filename, 'w') as file:
    json.dump(username, file)
    print("well remember you when you come back {} !".format(username))


"""Example of Read"""
with open(filename, 'r') as file:
    username = json.load(file)
    print("welcome back {}".format(username))


"""Example of json asking of username with (argv)"""
import json
import sys

username = input("please enter your username")
#filename = 'username.json'
filename = sys.argv[1]

try:
    with open(filename) as file:
        username = json.load(file)
except FileNotFoundError:
    username = input('whats your username')
    with open(filename, 'w') as file:
        json.dump(username, file)
        print("well remember you when you come back " + username)
else:
    print("welcome back "+ username +" !")
