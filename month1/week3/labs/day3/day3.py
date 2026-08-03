# Exception Handling & Defensive Programming
# Part A — What Is an Exception?

number = int(input("Enter a number: "))
print(number) # ValueError: invalid literal for int() with base 10: 'hello'
# That's an exception. An exception means: "I don't know how to continue."

# Mini Exercise 1: A (No Running)
int("python") # ValueError: invalid literal for int() with base 10: 'python'

# Mini Exercise 1: B (No Running)
numbers = [1, 2]
print(numbers[5]) # IndexError: list index out of range

# Mini Exercise 1: C (No Running)
print(score) # NameError: name 'score' is not defined

# Part B - Handling Exceptions
# Instead of the code below crashing:
number = int(input("Enter a number: "))

# we can write
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.") # Now the program continues running.

try:
    risky_code()

except ValueError:
    handle_error() # Python: Executes the try block. If nothing goes wrong, skips except. If a ValueError occurs, jumps to except.

# Think of `try` like this:  "Attempt this." Think of `except` as: "If it fails in this specific way, here's what to do instead.
# An exception means: "I don't know how to continue."

# Part C - Multiple Exceptions
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...  # Each except handles a different problem.

# Part D - else: Most beginners never learn this.   
try:
    number = int(input())

except ValueError:
    print("Invalid input")

else:
    print("Success!") # The else block runs only if no exception occurred.

# Part E - finally: The finally block always runs. Whether: success ✅, failure ✅. Examples: close database connections, close files, release resources
try:
    ...
except:
    ...
finally:
    print("Finished.")

# Part F — Defensive Programming
# improve one of your earlier functions.
# Original:

def sum_positive(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number

    return total

# Question: What if someone calls:
sum_positive(None) or sum_positive("hello") # The function crashes. Professional engineers think: "How can I make my function fail gracefully or clearly?"
def sum_positive(numbers):
    if numbers is None:
        raise ValueError("numbers cannot be None")
    
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total # Now the error is immediate and informative.

# Assertion: An assertion is a statement that says: "This must be true."
age = 25
assert age > 0 # Nothing happens. Because the statement is true.

age = -5
assert age > 0 # Python raises: AssertionError because the assumption was violated.

# Engineers Use Assertions because suppose you're writing:

def calculate_average(scores):
    ...

# You might assert:
assert len(scores) > 0
# because calculating an average of an empty list doesn't make sense. Assertions help catch bugs early during development.

# Practice Questions (No Code Yet): Tell me what happens in each case.
# Part A
x = 10
assert x > 0 # Nothing happens. Because the statement is true.

# Part B
x = -10
assert x > 0 # Python raises: AssertionError because the assumption was violated.

# Part C
names = []
assert len(names) > 0 # Python raises: AssertionError because the assumption was violated.

