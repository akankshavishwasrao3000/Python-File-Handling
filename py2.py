sname=input('enter the name of studant: ')
rollname=int(input('enter the roll number : '))

sub1=int(input("enter the marks of sub1 : "))
sub2=int(input("enter the marks of sub2 : "))
sub3=int(input("enter the marks of sub3 : "))

total=sub1+sub2+sub3
perct=total/3

print("Studant name: ",sname)
print("Roll Number : ",rollname)
print(" Math : ",sub1)
print(" elect : ",sub2)
print(" comp : ",sub3)
print(" Total : ",total)
print(" percentage : ",float(perct),'%')




