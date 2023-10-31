try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result of {num1} / {num2} is {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("program finished.")
