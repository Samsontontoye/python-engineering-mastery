# Building New Collections

# exercise 1: Build a new list containing only the even numbers.
# expected output: [2,4,6]
numbers = [1,2,3,4,5,6]

even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(even) 

# exercise 2: Create a new list containing the squares.
# expected output: [1,4,9,16]
numbers = [1,2,3,4]

squares = []

for number in numbers:
        squares.append(number ** 2)
print(squares)

# exercise 3: Build a new list where every name is uppercase.

names = ["samson", "ada", "john"]

new_names = []

for name in names:
        new_names.append(name.upper())
print(new_names)

# exercise 4: Return every number greater than 5.
numbers = [8,2,10,5,7]

higher_number = []

for number in numbers:
    if number > 5:
        higher_number.append(number)
print(higher_number)

# exercise 5: Return only words longer than four letters.
words = ["python","java","go","rust"]

long_letters = []

for word in words:
    if len(word) > 4:
        long_letters.append(word)
print(long_letters)

# interview problem
# Given the list below, write a function that collects the even number and stores them in a list
# expected output: [4, 2, 6, 8]
numbers = [4,7,2,9,6,8]

def collect_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
print(collect_even(numbers))

numbers = [1, 2, 3]

new_numbers = numbers.copy()

new_numbers.append(4)

print(numbers)
print(new_numbers)

