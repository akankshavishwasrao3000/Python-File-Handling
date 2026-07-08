with open("Employee.txt","w") as f:
    f.write("\nEmployee ID : 120")
    f.write("\nEmployee Name : Akanksha Ramesh Vishwasrao. ")
    f.write("\nEmployee Salary : 90000/-")
    f.write("\nEmployee Deparment : Computer Enginer.")
print("Writting done...")    

with open("Employee.txt","r") as f:
    content=f.read()
    print(content)
print("Reading Done.......")    
   