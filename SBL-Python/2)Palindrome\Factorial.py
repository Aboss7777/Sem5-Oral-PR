def is_palindrome(s):
    rev = s[::-1]
    if s==rev :
        return True
    else :
        return False

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    print("Menu:")
    print("1. Check if a string is palindrome")
    print("2. Find the factorial of a number")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        string_input = input("Enter a string: ")

        if is_palindrome(string_input) == True:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

    elif choice == '2':
        num = int(input("Enter a number: "))

        result = factorial(num)

        print(f"The factorial of {num} is {result}")

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3).")
