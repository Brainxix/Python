print("Simple calculator")

num1 = float(input(" Enter the first number: "))
num2 = float(input(" Enter the second number: "))

print("Enter your preferred operator +, -, *, /")
op = input(" Enter your preferred operator: ")
if op == "+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op =="*":
    print(num1 * num2)
elif op =="/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error, cannot divide by zero")
else:
    print("no operator in the list operators")
