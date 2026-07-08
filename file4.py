class Account:
    def __init__(self,accno,cutname,accbal):
        self._accno=accno
        self._cutname=cutname
        self.accbal=accbal


    @property
    def accno(self):
        return self._accno
    

    @accno.setter
    def accno(self,accno):
        self.accno=accno

    @property
    def cutname(self):
        return self._cutname

    @cutname.setter
    def custname(self,cutname):
        self.cutname=cutname

    @property
    def accbal(self):
        return self._accbal

    @accbal.setter
    def accbal(self,new_accbal):
        self._accbal =new_accbal
    

accno=int(input("Enter the Account Number : "))
cutname=input("Enter the Custmar Name : ")
accbal=int(input("Enter the Account Balance : "))


obj=Account(accno,cutname,accbal) #create Object

with open("python.txt","x") as f: #create new file (error if file already created.)
    f.write(str(obj.accno))
    f.write(obj.cutname)
    f.write(str(obj.accbal))
print("Writting Done...............")

with open("accfile.txt") as f:
    content=f.read()
    print(content)


#FileExistsError: [Errno 17] File exists: 'py2.py'
'''
In Python file handling, 'x' is a file mode used with the open() function. It stands for exclusive creation.

Purpose of 'x' mode:
The primary purpose of the 'x' mode is to create a new file, but only if a file with the same name does not already exist.

Behavior:
If the specified file does not exist, Python will create it and open it for writing.
If a file with the same name already exists, Python will raise a FileExistsError.
 
 
 
 
 '''           
        