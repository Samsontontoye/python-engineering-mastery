# Part 1 — Pattern Recognition Quiz
# Question 1: Given numbers = [8,3,5,1,6,3]. Return: True if a duplicate exists.
# Pattern? The pattern is fast lookup
# Data structure? The data structure is set
# Time complexity?: The time complexity is O(n)

# Question 2: Given word = "programming" Return {'p':1, 'r':2,...}
# Pattern? The pattern is frequency counting
# Data structure? The data structure is dictionary
# Time complexity?: The time complexity is O(n)

# Question 3: Given numbers = [2,7,11,15] target = 9. Return [0,1]
# Pattern? The pattern is dictionary lookup pattern
# Data structure? The data structure is dictionary
# Time complexity?: The time complexity is O(n)

# Question 4: Given word1 = "listen" word2 = "silent"
# Pattern? The pattern is frequency counting + hash maps 
# Data structure? The data structure is dictionary
# Time complexity?: The time complexity is O(n)

# Question 5: Given
# emails = [
# "a@gmail.com",
# "b@gmail.com",
# "a@gmail.com"
# ]
# Need to know if an email already exists.
# Pattern? The pattern is fast lookup
# Data structure? The data structure is set
# Time complexity?: The time complexity is O(n)

# Part 2 — Complexity Quiz: No coding. Just answer. 1. dictionary["age"]. Time complexity? 
# The time complexity is O(1)
# 2. set.add(5): The time complexity is O(1)
# 3. sorted(numbers): The time complexity is O(n log n)
# 4. for i in numbers:
#     print(i)
# The time complexity is O(n)   
# 5. for i in numbers:
#     for j in numbers:
#         print(i,j)
# The time complexity is O(n²)
# 6. 5 in my_set: The time complexity is O(1)
# 7. len(dictionary): The time complexity is O(1)
# 8. list.append(5): The time complexity is O(1)

# Part 3 — Mixed Coding Exercises
# Weekly Pattern Review & Mock Interview #1
# Exercise 1: Write contains_duplicate(numbers) Example [8,3,5,1,6,3] Return True
numbers = [8,3,5,1,6,3]

def contains_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

print(contains_duplicate(numbers))

# Exercise 2: Write character_frequency(word). Example "apple" Return {'a':1, 'p':2, 'l':1, 'e':1}
word = "apple"

def character_frequency(word):
    freq = {}
    for character in word:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1
    return freq

print(character_frequency(word))

# OR
def character_frequency(word):
    freq = {}
    for character in word:
        freq[character] = freq.get(character, 0) + 1
    return freq
print(character_frequency(word))

# Exercise 3: Write first_duplicate(numbers) Example [4,5,1,2,0,4,1] Return 4
numbers = [4,5,1,2,0,4,1]

def first_duplicate(numbers):
    result = set()
    for number in numbers:
        if number in result:
            return number
        result.add(number)
    return None

print(first_duplicate(numbers))

# Exercise 4: Write same_frequency(word1, word2) Return True or False
word1 = "silent"
word2 = "listen"

def same_frequency(word1, word2):
    if len(word1) != len(word2):
        return False
    
    freq1 = {}
    freq2 = {}

    for character in word1:
        freq1[character] = freq1.get(character, 0) + 1
    
    for character in word2:
        freq2[character] = freq2.get(character, 0) + 1

    return freq1 == freq2

print(same_frequency(word1, word2))

# Exercise 5 Solve Two Sum without looking at your notes.
numbers = [3, 2, 4]
target = 6

def two_sum(numbers, target):
    lookup = {}
    for index, number in enumerate(numbers):
        numbers_needed = target - number
        if numbers_needed in lookup:
            return [lookup[numbers_needed], index]
        lookup[number] = index

print(two_sum(numbers, target))

# Exercise 6: Write remove_duplicates(numbers) Example [1,2,2,3,3,4] Return [1,2,3,4]. Try to preserve the original order.
numbers = [1,2,2,3,3,4]

def remove_duplicates(numbers):
    return(set(numbers))

print(remove_duplicates(numbers))

# OR
def remove_duplicates(number):
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result

print(remove_duplicates(numbers))

# Exercise 7: Write most_frequent_number(numbers) Example [2,4,2,1,2,4] Return 2

numbers = [2,4,2,1,2,4]

def most_frequent_number(numbers):
    count = {}
    # count each number
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    # most frequent appearing letter
    most_frequent = None
    highest_count = 0

    for number in count:
        if count[number] > highest_count:
            highest_count = count[number]
            most_frequent = number
    return most_frequent
print(most_frequent_number(numbers))

# Exercise 8: Given list1 = [1,2,3], list2 = [3,4,5]. Return [3]

list1 = [1,2,3]
list2 = [3,4,5]

set1 = set(list1)
set2 = set(list2)

print(list(set1 & set2))

# Exercise 9: Write build_lookup(numbers) Example [7,9,3] Returns {7:0, 9:1, 3:2}
numbers = [7,9,3]

for index, number in enumerate(numbers):
        print({number: index})

# OR 
lookup = {}

for index, value in enumerate(numbers):
       lookup[value] = index

print(lookup)

# Exercise 10 Problem: Given numbers = [2,4,5,7,4,8] Return 1. Return: the index of the first occurrence, not the duplicate value.
# Example: Index:   0 1 2 3 4 5 Value: 2 4 5 7 4 8. The duplicated value is 4. Its first occurrence is at index 1.
# So the answer is: 1

# Step 1 : we are going to loop through the list and once the first duplicate value is detected, return the index of the first duplicate value 
# Step 2: The pattern is dictionary lookup and the data structure is dictionary 
# Step 3: The time complexity is O(n) and the space complexity is O(n) 
# Step 4: The code is below

numbers = [2,4,5,7,4,8]

def return_first_duplicate_number(numbers):
    lookup = {}
    for index, number in enumerate(numbers):
        if number in lookup:
            return[lookup[number]]
        lookup[number] = index

print(return_first_duplicate_number(numbers))
