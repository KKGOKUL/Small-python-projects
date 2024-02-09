print("SIMPLE CALCULATER")
print()
print("""Choose which operation do you want to perform?
       Select as follow""")

print("""
      1.Addition
      2.Substraction
      3.Multiplication
      4.Division
      """)
operation=int(input(">>>"))

if operation==1:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Addition is:",num1+num2)


elif operation==2:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Substraction is:",num1-num2)

elif operation==3:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Multiplication is:",num1*num2)

elif operation==4:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Division is:",num1/num2)

else:
    print("Invalid entry,Please enter correct operation!")

    
