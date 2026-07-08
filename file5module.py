from file5 import*

lst=[]
while(True):
    accno=int(input("Enter the Account Number : "))
    cutname=input("Enter the Custmar Name : ")
    accbal=int(input("Enter the Account Balance : "))
    obj=Account(accno,cutname,accbal) #create Object
    lst.append(obj)
    ct=int(input("Do you want to add next data press 1 : "))
    if ct !=1:
        break

with open("accfile.txt","w") as f: 
    f.write(str(obj.accno))
    f.write(obj.cutname)
    f.write(str(obj.accbal))
print("Writting Done...............")

with open("accfile.txt") as f:
    content=f.read()
    print(content)

