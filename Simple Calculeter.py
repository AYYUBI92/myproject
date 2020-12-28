num1 = int(input("Enter Your First Numbers: "))
operator = input("Enter Operator")
num2 = int(input("Enter Your Second Numbers: "))
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