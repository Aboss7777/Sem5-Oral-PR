n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

temp = 0

temp = n1
n1 = n2
n2 = temp

print(f"Swapped values: n1 = {n1}, n2 = {n2}")

if n1 > 0:
    print("The number is positive")
elif n1 == 0:
    print("The number is zero")
else:
    print("The number is negative")
