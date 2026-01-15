num=int(input("Enter first number: "))
num1=int(input("Enter second number: "))
choice=int(input("Enter 1 for addition, 2 for multiplication, 3 for subtraction: "))
if choice==1:
    result=num+num1
    print("Addition:",result)
elif choice==2:
    result=num*num1
    print("Multiplication:",result)
elif choice==3:
    result=num-num1
    print("Subtraction:",result)
else:
    print("Invalid choice")
def addition():
    add=num+num1
    print(add)
addition()
def multiplication():
    mult=num*num1
    print(mult)
multiplication()
def subtraction():
    sub=num-num1
    print(sub)
subtraction()
