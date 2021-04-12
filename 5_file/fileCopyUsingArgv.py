from sys import argv

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")
print("if you want press e or exit to exit")

i = input("yes/no")
if i == "e" or i == "exit":
    exit(0)

file_1 = fopen(from_file)
file_1 = file_1.read()

print(f"print the input file is {len(file_1)} ")
print("does the out file exist ?")

file_2 = open(to_file, 'w')
file_2.write(file_1)
print("all done")
file_2.close()
file_1.close()


