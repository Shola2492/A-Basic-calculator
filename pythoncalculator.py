# python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st operator: "))
num2 = float(input("Enter the 2nd operator: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not a valid operator")