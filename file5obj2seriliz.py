from file5 import*
import pickle

accno=int(input("Enter the Account Number : "))
cutname=input("Enter the Custmar Name : ")
accbal=int(input("Enter the Account Balance : "))

obj=Account(accno,cutname,accbal) #create Object

'''
# Serialize (pickle) the object to a file
pickle_data=pickle.dump(obj)

print("read object from file .....")
bankobj=pickle.loads(pickle_data)

print(bankobj.accno)
print(bankobj.cutname)
print(bankobj.accbal)
'''


with open("bankacc.txt","wb") as f: 
    pickle.dump(obj,f)
print("object saved successfully !.....")


with open("bankacc.txt" ,"rb") as f:
    content= pickle.load(f)
    print("loaded object : ",content)
    
    print(content.accno)
    print(content.cutname)
    print(content.accbal)


'''
Enter the Account Number : 456
Enter the Custmar Name : jack
Enter the Account Balance : 4500000
object saved successfully !.....
loaded object:  <file5.Account object at 0x000001BB3CB21D10>
456
jack
4500000


'''