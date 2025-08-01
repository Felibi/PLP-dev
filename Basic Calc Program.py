a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter mathematical operation: ")

if c == "+":
    d = int(a) + int(b)
    print(str(a) + "+" + str(b) + "=" + str(d))
elif c == "-":
    d = int(a) - int(b)
    print(str(a) + "-" + str(b) + "=" + str(d))
elif c == "*":
    d = int(a) * int(b)
    print(str(a) + "*" + str(b) + "=" + str(d))
elif c == "/":
    if int(b) != 0:
        d = int(a) / int(b)
        print(str(a) + "/" + str(b) + "=" + str(d))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")