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

with open("accfile.txt","a") as f:   # Here we use a (append()) it  add's new data at the end without deleting old content.
    f.write(str(obj.accno))
    f.write(obj.cutname)
    f.write(str(obj.accbal))
print("Writting Done...............")

with open("accfile.txt") as f:
    content=f.read()
    print(content)


            
        