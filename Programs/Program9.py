Find the largest of three numbers.

a = int(input("Enter the First Number"))
b = int(input("Enter the Second Number"))
c = int(input("Enter the Third Number"))

if a > b:
    largest = a
else:
    largest = b

if c > largest:
    print("The largest number is:", c)
else:
    print("The largest number is:", largest)
