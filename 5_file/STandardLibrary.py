#import sys
from sys import argv
script, file_name = argv
print(f'so your file is {file_name}')

f = open(file_name)

print('here is your file name ')
print(f.read())
