Take two numbers from the user and print:

Addition
Subtraction
Multiplication
Division

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

Addition = a + b
Subtraction = a - b
Multiplication = a * b
if b != 0:
    Division = a / b
else:
    Division = "Undefined (Cannot divide by zero)"

print(f"The Addition of Two Numbers is {Addition}")
print(f"The Subtraction of Two Numbers is {Subtraction}")
print(f"The Multiplication of Two Numbers is {Multiplication}")
print(f"The Division of Two Numbers is {Division}")
