# Functions — Teaching the Computer to Reuse Work
def greet():
    print("Hello Samson")

greet()

# make the function reusable
def greet(name):
     print(f"Hello {name}")

greet("Samson")
greet("David")

# name is a parameter when you call greet("Samson"), "Samson" is the argument

# this
def square(number):
     print(number * number)

square(4)

# and this are not the same thing
def square(number):
     return number * number

x = square(5)
print(x)

def add(a, b):
     print(a + b)

result = add(5, 6)

def add(a, b):
     return a + b

result = add(5, 6)
print(result)

# find the largest value in the list without using sort or max
numbers = [3, 8, 2, 9]

# solution
largest = numbers[0]

for num in numbers:
     if num > largest:
         largest = num

print(largest)

# convert the above into a function
def find_largest_value(numbers):
     largest = numbers[0]
     for num in numbers[1:]:
         if num > largest:
             largest = num
     return largest

numbers = [3, 8, 2, 9]
print(find_largest_value(numbers))
print(find_largest_value([]))

# exercise 1
def introduce(name):
     print(f"Hello! My name is {name}")

introduce("Samson")

# exercise 2
def greet(name):
     print(f"Hello {name}")

greet("Benson")

# exercise 3
def multiply(a, b):
     return a * b

# exercise 4
result = multiply(5, 8)
print(result)

def greet(name):
    print(f"Hello {name}")

message = greet("Samson")

print(message)