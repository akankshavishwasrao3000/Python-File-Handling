from file5 import*

accno=int(input("Enter the Account Number : "))
cutname=input("Enter the Custmar Name : ")
accbal=int(input("Enter the Account Balance : "))
obj=Account(accno,cutname,accbal) #create Object

with open("accfile.txt","w") as f: 
    f.write(str(obj))
print("Writting Done...............")

with open("accfile.txt") as f:
    content=f.read()
    print(content)


# <file5.Account object at 0x000001EF15AD6A50> 
'''
This means you are seeing the default string representation of a Python object. Specifically:

<file5.Account object at 0x000001EF15AD6A50> tells you:
The object is an instance of the Account class from the file5 module.
The part after at (like 0x000001EF15AD6A50) is the memory address where this object is stored in your computer's memory.
'''
