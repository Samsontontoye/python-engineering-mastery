# Boolean Logic & Conditional Statements

print(10 > 5)
print(3 == 7)

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")

# exercise 1
temperature = 28

if temperature > 30:
    print("The weather is Hot")
else:
    print("The weather is warm")

# exercise 2
age = int(input("How old are you?: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# exercise 3
score = 76

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# exercise 4
is_logged_in = True

if is_logged_in:
    print("Welcome Back")
else:
    print("Kindly Login")

# interview problem
# given the below, write a function that returns the count of number of even integers in the list.
numbers = [8, 2, 10, 5, 7]

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

print(count_even(numbers))

age = 20

if age > 18:
    print("A")

if age > 10:
    print("B")

age = 20

if age > 18:
    print("A")
elif age > 10:
    print("B")

x = 5

if x > 3:
    print("A")

x = 1

if x > 3:
    print("B")

print("Done")