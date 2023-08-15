print("This is my First Assignment")

# print table
 # using for loop
print("             ")
print("printing table using for loop")
number = int(input("enter your number:"))
for i in range(1,11):
    print(number,"*",i,"=",number*i)


print("   ")
# while loop
print("Printing Table using While loop")
num = int(input("enter your number:"))
count =1
while count <= 10:
    num = num*1
    print(num,"*",count,"=",num*count)
    count+=1

#conditional statments 
print("Conditional Statments: ")
num1= int(input("enter num1 value:"))
num2= int(input("enter num2 value:"))
if num1 < num2:
    print(num2, " is biggest value")
elif num1 > num2:
    print(num1, " is biggest value")
else:
    print(num1," = ",num2)



print("      ")
print("Conditional Statmets with multiple elif condition")
#Conditional Statments with multiple elif condition   
name = input("enter student name:")
marks =int(input("enter marks of student:"))

if marks > 85 and marks <101:
    print(name,"is got a",marks," and his grade is A")
elif marks > 64 and marks < 85:
    print(name,"is got a",marks," and his grade is B")
elif marks > 39 and marks < 65:
    print(name,"is got a",marks," and his grade is C")
elif marks > 27 and marks < 40:
    print(name,"is got a",marks," and his grade is D")
elif marks >= 0 and marks <28:
    print(name,"is got a",marks," So his Faild")
else:
    print("Hello,",name,"You entered Worng Marks")

print("   ")

#logical Operator 
# AND :
print("AND Operator :")
a=10
print(a<0 and a>0 )
print(0<a and a>0 )
print(a>0 and a<0 )

print("   ")
# OR :
print("OR Operatior :")
print(a>0 or a<0 )
print(a<0 or 0>a )

print("       ")
# NOT :
print("NOT Operator :")
print(not a>0 )
print(not a<0 )


print("      ")
#Relational Operator
print("Relational Oprtator :")
x=10
y=20
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x == y)
print(x != y)
