import os
#1. Using OS library
print(os.getcwd())

#2.check whether specified path exists or not
print(f"Your base directory is: {os.getcwd()}")
#Make new directory from user input
dirname = input(f"Please enter a name for your new directory: ")
while not dirname:
    dirname = input(f"Please enter a name for your new directory: ")
if not os.path.isdir(dirname):
    os.mkdir(os.path.join(os.getcwd(), dirname))
os.chdir(dirname)
print(os.getcwd())
    
filename = input(f"Please enter a name for your new file: ")
while not filename:
    filename = input(f"Please enter a name for your new file: ")

with open("{}.txt".format(filename), "w+") as f:

    name = input(f"Please enter a name: ")

    address = input(f"Please enter an address: ")

    phone = input(f"Please enter a phone number: ")

    testlist = (name, address, phone)
    seperator = ","
    f.write(seperator.join(testlist))
with open("{}.txt".format(filename), "r") as f:
    print(f.readline())
