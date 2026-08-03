# Dictionaries (Hash Maps): The Most Important Python Data Structure for interviews
# Dictionary Syntax: Creating
person = {}
person = dict()
person["name"] = "Samson"
person["age"] = 31
print(person)

# Dictionary Syntax: Updating
person["age"] = 20
print(person)

# Dictionary Syntax: Remove
# person.pop("age")
# print(person)

# Dictionary Syntax: Reading
print(person["name"])

# Dictionary Syntax: Checking existence
if "name" in person:
    print("Found!")

# Dictionary Syntax: Length
print(len(person))

# Important Dictionary Methods: .get(). Instead of
# print(person["salary"]) # which causes KeyError, use
print(person.get("salary")) # Returns None or
print(person.get("salary", 0)) # Returns 0

# Important Dictionary Methods: .keys()
print(person.keys()) # Output dict_keys(["name","age"])

# Important Dictionary Methods: .values()
print(person.values())

# Important Dictionary Methods: .items()
print(person.items()) # or 

for key, value in person.items():
    print(key, value)

# Interview Pattern #1
# Frequency Counter
text = "banana"
freq = {}
for letter in text:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1
print(freq)

# Cleaner version
freq = {}
for letter in text:
    freq[letter] = freq.get(letter, 0) + 1
print(freq)

# Interview Pattern #2
# Fast Lookup. Instead of
numbers = [2, 5, 9, 13, 18]
for num in numbers:
    if num == target:

# Create
lookup = {}
for num in numbers:
    lookup[num] = True

# Now

if target in lookup: # is approximately O(1).

# Big-O Deep Dive: Suppose
numbers = [2, 5, 9, 13, 18] # Checking if 18 exists:

# Using a list
18 in numbers
# Worst case comparisons:
# 2
# ↓

# 5
# ↓

# 9
# ↓

# 13
# ↓

# 18

# Operations grow with the size of the list.

# If there are:

# 10 elements → up to 10 checks
# 1,000 elements → up to 1,000 checks
# 1,000,000 elements → up to 1,000,000 checks

# Time complexity: O(n)

# Using a dictionary
lookup = {
    2: True,
    5: True,
    9: True,
    13: True,
    18: True
}

18 in lookup

# Python hashes the key and jumps almost directly to its location.

# Whether there are:

# 10 items
# 1,000 items
# 1,000,000 items

# the average amount of work stays roughly constant.

# Time complexity:

# O(1) average

# Exercise 1. Given fruits = ["apple", "banana", "apple", "orange", "banana", "apple"], return {"apple": 3, "banana": 2, "orange": 1}
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

def count_of_fruits(fruits):
    freq = {}
    for fruit in fruits:
        if fruit in freq:
            freq[fruit] += 1
        else:
            freq[fruit] = 1
    return freq

print(count_of_fruits(fruits))

# Exercise 2 (Easy). Given student = {"name": "Alice", "age": 20, "grade": "A"}. Print every key and value using .items().
student = {"name": "Alice", "age": 20, "grade": "A"}

for key, value in student.items():
    print(key, value)

# Exercise 3 (Easy–Medium). Given numbers = [4, 8, 15, 16, 23, 42]. Build a dictionary where every number is a key and the value is True.
# Then determine whether 15 and 100 exist using dictionary membership.
numbers = [4, 8, 15, 16, 23, 42]

lookup = {}

for number in numbers:
    lookup[number] = True

# or(dictionary comprehension(another solution))
lookup = {num: True for num in numbers}

print(lookup)
print(lookup)
print(15 in lookup)
print(100 in lookup)

# Exercise 4 (Medium). Given text = "mississippi". Return the frequency of each character using the .get() pattern.
text = "mississippi"

freq = {}
for letter in text:
    freq[letter] = freq.get(letter, 0) + 1
print(freq)

# Exercise 5 (Medium). Given words = ["cat", "dog", "cat", "bird", "dog", "dog"]. Find the most frequent word.
# Try solving it in a single pass after building the frequency dictionary.
words = ["cat", "dog", "cat", "bird", "dog", "dog"]

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)

# or(another solution) 
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

# find the most frequent word
def most_frequent(words):
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    most_common = None
    highest_count = 0

    for word, count in freq.items():
        if count > highest_count:
            highest_count = count
            most_common = word

    return most_common

# Exercise 6: Interview Style. Without using collections.Counter, determine whether two strings are anagrams. Example: "listen","silent" Output: True
# Example: "apple","papel" Output: True. Example: "rat", "car". Output: False
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    freq1 = {}
    freq2 = {}

    for letter in s:
        freq1[letter] = freq1.get(letter, 0) + 1

    for letter in t:
        freq2[letter] = freq2.get(letter, 0) + 1

    return freq1 == freq2

print(is_anagram("listen", "silent"))

# Exercise 7: Build a frequency dictionary for: word = "programming". Expected output:{'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}
word = "programming"

def freq_dict(word):
    freq = {}
    for letter in word:
            freq[letter] = freq.get(letter, 0) + 1
    return freq

print(freq_dict(word))

# Exercise 8: Write a function: same_frequency(word1, word2). It should return the two frequency dictionaries, 
# for example: same_frequency("cat", "tac") returns ({'c':1,'a':1,'t':1}, {'t':1,'a':1,'c':1})
# Don't compare them yet—just build and return both dictionaries.

def same_frequency(word1, word2):

    freq1 = {}
    freq2 = {}
    
    for letter in word1:
        freq1[letter] = freq1.get(letter, 0) + 1

    for letter in word2:
        freq2[letter] = freq2.get(letter, 0) + 1
    
    return freq1, freq2
    
print(same_frequency("cat", "tac"))

# Exercise 9: Modify Exercise 8 so it returns: True. if the dictionaries are equal, otherwise False
def same_frequency(word1, word2):
    if len(word1) != len(word2):
        return False
    
    freq1 = {}
    freq2 = {}

    for letter in word1:
        freq1[letter] = freq1.get(letter, 0) + 1

    for letter in word2:
        freq2[letter] = freq2.get(letter, 0) + 1
    
    return freq1 == freq2
    
print(same_frequency("cat", "tac"))

# Exercise 10 – Count Numbers. Given: numbers = [1, 2, 2, 3, 1, 4, 2, 5]. Return:{1: 2, 2: 3, 3: 1, 4: 1, 5: 1}
numbers = [1, 2, 2, 3, 1, 4, 2, 5]

def count_number(numbers):
    freq = {}
    for number in numbers:
        freq[number] = freq.get(number, 0) + 1
    return freq

print(count_number(numbers))

# Exercise 12 – Count Characters. Given: text = "hello world" Count every character. Expected:{'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}
text = "hello world"

def count_characters(text):
    freq = {}
    for letter in text:
        freq[letter] = freq.get(letter, 0) + 1
    return freq

print(count_characters(text))

# Exercise 13 - Given: sentence = "python is fun python is awesome". Split the sentence into words and count each word. 
# Expected: {'python':2, 'is':2, 'fun':1, 'awesome':1}. Hint: sentence.split()
sentence = "python is fun python is awesome"

def count_sentence(sentence):
    freq = {}
    for word in sentence.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(count_sentence(sentence))

# Exercise 14 – Highest Score. Given: scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}. Return "David". Do not use max().
scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}

def highest_score(scores):
    for key, value in scores.items():
        if value > 91:
            return key
    return None
print(highest_score(scores))

# Exercise 15 – Lowest Score. Given: scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}. Return "Charlie". Do not use min().
scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}

def lowest_score(scores):
    for key, value in scores.items():
        if value < 80:
            return key
    return None
print(lowest_score(scores))

# Exercise 16 – Average Score. Given: scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}. Return the average score. Do not use sum().
scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}

def average_scores(scores):
    total = 0
    for score in scores.values():
        total += score
    average = total/len(scores)
    return average

print(average_scores(scores))

# Exercise 17: Frequency Pattern – First Repeated Number. Given numbers = [3,7,2,5,7,9], Return 7. 
# Hint: Use a dictionary. As soon as you see a number twice... Return it.
numbers = [3,7,2,5,7,9]

def repeated_number(numbers):
    seen = {}
    for number in numbers:
        if number in seen:
            return number
        seen[number] = True 
    return None
print(repeated_number(numbers)) 

# Exercise 18 – First Non-Repeated Number. Given numbers = [4,5,1,2,0,4,1,2] Return 5. Why? Because it appears exactly once.
numbers = [4,5,1,2,0,4,1,2]

def first_non_repeated_number(numbers):
    freq = {}
    # counting frequency
    for number in numbers:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1

    # find the number that appears once
    for number in numbers:
        if freq[number] == 1:
            return number
    return None

print(first_non_repeated_number(numbers))

# Exercise 19 – Duplicate Detection. Given numbers = [8,3,5,1,6,3], Return True because a duplicate exists.
# If numbers = [8,3,5,1]. Return False
numbers = [8,3,5,1,6,3]

def duplicate_detection(numbers):
    seen = {}
    for number in numbers:
        if number in seen:
            return True
        seen[number] = True
    return False

print(duplicate_detection(numbers))

# Exercise 20 – Count Even Numbers. Given numbers = [2,4,5,6,8,9,10], Return {2:1, 4:1, 6:1, 8:1, 10:1}. Ignore odd numbers.
numbers = [2,4,5,6,8,9,10]

def count_even_numbers(numbers):
    count = {}
    for number in numbers:
        if number % 2 == 0:
            count[number] = count.get(number, 0) + 1
    return count
        
print(count_even_numbers(numbers))