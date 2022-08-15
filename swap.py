a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

a = a - b
b = a + b
a = b - a

print(f"After swap, first number is: {a}")
print(f"After swap, second number is: {b}")