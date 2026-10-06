# Question 2 - Unbreakable Program
# A program that keeps running even when the user enters bad input.

def safe_input():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("That is not a number. Try again.")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Test: keep asking until the user enters a valid number
print("Welcome to the unbreakable calculator!")
number = safe_input()
print("You entered:", number)

# Test: division that handles zero
print("Dividing 100 by your number...")
print("Result:", safe_divide(100, number))