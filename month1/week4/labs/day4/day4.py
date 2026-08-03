# Hash Map Lookup Pattern
# Guided NeetCode Problem – Two Sum
# Given an array of integers and a target number, return the indices of the two numbers that add up to the target.
numbers = [3, 8, 2, 5, 11, 6, 9, 15]
target = 9

# brute force solution
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]

print(two_sum(numbers, target)) # Complexity Analysis: Time complexity is O(n²) and space complexity is O(1)

# Optimized Solution
numbers = [3, 2, 4]
target = 6

def two_sum(numbers, target):
    lookup = {}
    for index, number in enumerate(numbers):
        number_needed = target - number
        if number_needed in lookup:
            return[lookup[number_needed], index]
        lookup[number] = index

print(two_sum(numbers, target))

# What Is enumerate()?
# Normally, you might write:
numbers = [2, 7, 11, 15]
for i in range(len(numbers)):
    print(i, numbers[i])

# output:
# 0 2
# 1 7
# 2 11
# 3 15

# enumerate() gives you the same information in a cleaner way:
# numbers = [2, 7, 11, 15]
# for index, number in enumerate(numbers):
#     print(index, number)

# output:
# 0 2
# 1 7
# 2 11
# 3 15

# Think of enumerate() as: "Give me both the position(index) and the value."
# if enumerate() still feels unfamiliar, the solution can also be written like this:

numbers = [3, 2, 4]
target = 6

def two_sum(numbers, target):
    lookup = {}
    for index in range(len(numbers)):
        number = numbers[index]
        number_needed = target - number
        if number_needed in lookup:
            return[lookup[number_needed], index]        
        lookup[number] = index

print(two_sum(numbers, target))

# Exercise 1. Given:target = 10, number = 4. What is the needed value?
target = 10
number = 4

def needed_value(target, number):
        number_needed = target - number
        return number_needed

print(needed_value(target, number))

# Exercise 2: Create a dictionary that stores: value → index for numbers = [8, 3, 5]
# Expected result: {8: 0, 3: 1, 5: 2}
numbers = [8, 3, 5]

for index, value in enumerate(numbers):
        print({index: value})

# OR

lookup = {}

for index, value in enumerate(numbers):
    lookup[value] = index

print(lookup)
                
# Exercise 3. Explain in your own words: Why do we store the index instead of just the number?
# We store the index instead of the number because that's what the question asked.
# The problem asked to get the index and not values.
# We store the index because the problem requires us to return the positions of the two numbers, 
# not the numbers themselves. A dictionary lets us quickly retrieve the index of a previously seen value.

# Exercise 4 Medium: Write a function: def find_complement(numbers, target):
# Instead of returning indices, return the first complement pair of values.
# Example: numbers = [2, 7, 11, 15], target = 9. Return: (2, 7)
numbers = [2, 7, 11, 15]
target = 9

def find_complement(numbers, target):
     lookup = {}
     for index, number in enumerate(numbers):
          numbers_needed = target - number
          if numbers_needed in lookup:
               return [lookup[numbers_needed], number]
          lookup[number] = number

print(tuple(find_complement(numbers, target)))

# Exercise 5: Rewrite today's optimized solution without using enumerate(). Use range(len(numbers)) instead.
numbers = [3, 2, 4]
target = 6

def two_sum(numbers, target):
     lookup = {}
     for index in range(len(numbers)):
          number = numbers[index]
          numbers_needed = target - number
          if numbers_needed in lookup:
               return[lookup[numbers_needed], index]
          lookup[number] = index

print(two_sum(numbers, target))

# Exercise 6. Given: numbers = [5, 8, 12]. Build the lookup dictionary step by step. Write the dictionary after each iteration.
numbers = [5, 8, 12]

lookup = {}

for number in numbers:
    lookup[number] = True

print(lookup)
print(8 in lookup)     
print(10 in lookup)   

# Exercise 7: Pattern Building: Given: numbers = [4, 6, 1, 9], target = 10
# Without writing code, list: Current number Needed value
# Dictionary contents after each step
# The current number is : 4
# The needed value is needed = target(10) - current_number(4) = 6
# Dictionary contents after each step : {4: True, 6: True}

# Exercise 8: Exercise 8 Explain why the optimized solution is O(n) instead of O(n²). Use your own words.
# Because we are looping through the list once in order to find the two values that sum up to the target values.
# Once we find both values that sum up to the target value, we end the lookup.
# Each dictionary lookup is O(1), so even though we perform one lookup for every element, the overall time remains O(n).

# Exercise 9: Solve the full Two Sum problem using the optimized dictionary solution. Do not look back at the lesson while coding.
numbers = [3, 2, 4]
target = 6

def two_sum(numbers, target):
    lookup = {}
    for index, number in enumerate(numbers):
        number_needed = target - number
        if number_needed in lookup:
            return[lookup[number_needed], index]
        lookup[number] = index

print(two_sum(numbers, target))

# Exercise 10 Stretch Challenge: Modify your Two Sum solution so it returns: None
# instead of raising an error when no pair exists.
numbers = [3, 5, 4]
target = 6

def two_sum(numbers, target):
    lookup = {}
    for index, number in enumerate(numbers):
        number_needed = target - number
        if number_needed in lookup:
            return[lookup[number_needed], index]
        lookup[number] = index
    return None

print(two_sum(numbers, target))

# 1. lookup[number] = index. The time complexity is O(1) because we are not looping. We are inserting one key-value pair into a dictionary

# 2. needed in lookup. The time complexity is O(1)

# 3. for number in numbers:

#     print(number)

# The time complexity is O(n)

# 4. for i in range(len(numbers)):

#     for j in range(i + 1, len(numbers)):

#         pass

# The time complexity is O(n²)

# 5. numbers.sort(). The time complexity is O(n log n)