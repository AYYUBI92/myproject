num1 = int(input("Enter Your First Numbers: "))
#Create First User input Var
operator = input("Enter Operator")
#Create Operator Variable
num2 = int(input("Enter Your Second Numbers: "))
#Create Second User Input Variable
if operator == "+":
    print(num1 + num2 )
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
