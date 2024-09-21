# Python Calculator

operator = input("Enter an Operator ( + - * / )");
num1 = int(input("Enter the first Number"));
num2 = int(input("Enter the second number"));

if operator == '+':
    result = num1 + num2
    print(round(result,3))
elif operator == '-':
    result = num1 - num2
    print(round(result,3))
elif operator == '*':
    result = num1 * num2
    print(round(result,3))
elif operator == '/':
    result = num1 / num2
    print(round(result,3))
else:
    print(f"{operator} is not a valid operator")

