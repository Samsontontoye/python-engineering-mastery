# Common problem patterns

# Searching Problem → Find the first item that matches. ( Examples: Find the first even number, Find the first negative number, Find the longest word, 
# Find the smallest number, Find the first customer over 18)

# Counting Problem → Count how many items match. (Examples: Count vowels, Count positive numbers, Count customers in Lagos
# Count words longer than five characters, Count duplicates)

# Filtering/Collect Problem → Keep only the items that match.(Examples: Collect even numbers, Collect names beginning with A
# Collect positive transactions, Collect uppercase words)

# Accumulation/Aggregate Problem → Build up a result (such as a sum, product, or average). (Examples: Sum numbers, Average
# Maximum, Minimum, Total profit)

# Frequency Counting Problem → Use a dictionary to count how often each value appears.

# Problem 1: Given numbers = [3, 8, -2, 12, -5, 7], write a function sum_positive(numbers) that returns the total 30.
# Problem - Sum Positive Numbers
# Difficulty: ⭐☆☆☆☆
# Pattern Focus: Aggregate

numbers = [3, 8, -2, 12, -5, 7]

def sum_positive(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

print(sum_positive(numbers))

# Problem 2: Given: words = ["apple", "hi", "banana", "go", "orange"]. Write: collect_long_words(words)
# and return ["apple", "banana", "orange"]. A long word is any word with more than 4 characters.
# Problem - Collect Long Words
# Difficulty: ⭐☆☆☆☆
# Pattern: Collect

words = ["apple", "hi", "banana", "go", "orange"]

def collect_long_words(words):
    result = []
    for word in words:
        if len(word) > 4:
            result.append(word)
    return result
print(collect_long_words(words))

#  Problem 3: Given scores = [45, 82, 91, 67, 55, 100], count the high scores and return the count. write count_high_scores(scores) and return 3
# Problem - Count high scores
# Difficulty: ⭐☆☆☆☆
# Pattern: Count

scores = [45, 82, 91, 67, 55, 100]

def count_high_scores(scores):
    count = 0
    for score in scores:
        if score >= 80:
            count += 1
    return count

print(count_high_scores(scores))

# Problem 4: Given numbers = [2, 14, 9, 18, 25, 40, 7], Write collect_even_greater_than_ten(numbers) and Return [14, 18, 40]
# Problem - Collect with Two Conditions
# Difficulty: ⭐☆☆☆☆
# Pattern: Collect

numbers = [2, 14, 9, 18, 25, 40, 7]

def collect_even_greater_than_ten(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0 and number > 10:
            result.append(number)
    return result

print(collect_even_greater_than_ten(numbers))

# Problem 5: Given numbers = [5, -2, 8, -7, 10], Return the sum of even numbers only. This combines: Aggregate, Filtering
# Problem - Aggregate with a Condition
# Difficulty: ⭐☆☆☆☆
# Pattern: Aggregate

numbers = [5, -2, 8, -7, 10]

def sum_even_numbers(numbers):
    total_even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            total_even_numbers += number
    return total_even_numbers

print(sum_even_numbers(numbers))

# Problem 6: Given words = ["cat", "dog", "elephant", "ant"]. Return the first word longer than five characters. The expected output is elephant
# The requirement is: Return the first word longer than five characters.
# Whenever you see the word: "first" What pattern should immediately pop into your head? Not Collect. "Search".
# Because once you find the first match, you can stop.
# Difficulty: ⭐☆☆☆☆
# Pattern: Search

words = ["cat", "dog", "elephant", "ant"]

def words_longer_than_five_characters(words):
    for word in words:
        if len(word) > 5:
            return word
    return None

print(words_longer_than_five_characters(words))

# Problem 7 — Code Review: A junior engineer wrote:

def collect_even(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            print(number)

    return result

# Questions and answer
# Does the function do what its name promises? No it doesn't 
# What bug exists? The print(number) is the bug. It is supposed to return the result 
# How would you fix it? I will fix it by appending the number to the result variable and returning the result. 
# Then to use the function, i will print(collect_even(numbers))

# result
def collect_even(numbers): 
    result = [] 
    for number in numbers: 
        if number % 2 == 0: 
            result.append(number) 
    return result 
print(collect_even(numbers))


# Problem #8 — Search
# Given: numbers = [-4, -8, 3, -1]. Write: find_first_positive(numbers) Return: 3. If no positive number exists, return None
# Problem - Find first positive number. Whenever you see the word: "first" What pattern should immediately pop into your head? Not Collect. "Search".
# Because once you find the first match, you can stop.
# Difficulty: ⭐☆☆☆☆
# Pattern: Search

numbers = [-4, -8, 3, -1]

def find_first_positive(numbers):
    for number in numbers:
        if number > 0:
            return number
    return None

print(find_first_positive(numbers))

# Problem 9 — Count
# Given: words = ["apple", "hi", "banana", "go", "orange"]. Return the number of words longer than four characters.
# Pattern - Count
# Difficulty: ⭐☆☆☆☆

words = ["apple", "hi", "banana", "go", "orange"]

def count_words_longer_than_four(words):
    count = 0
    for word in words:
        if len(word) > 4:
            count += 1
    return count

print(count_words_longer_than_four(words))

# Problem 10 — Collect
# Given: numbers = [12, 5, 18, 3, 25, 40]. Return every number divisible by 3.
# Pattern - Collect
# Difficulty: ⭐☆☆☆☆

numbers = [12, 5, 18, 3, 25, 40]

def collect_numbers_divisible_by_3(numbers):
    result = []
    for number in numbers:
        if number % 3 == 0:
            result.append(number)
    return result

print(collect_numbers_divisible_by_3(numbers))

# Problem 11 — Aggregate
# Given: numbers = [8, -5, 10, 3, -2]. Return the sum of positive even numbers. Notice... Now we're combining: Aggregate, Filter, Two conditions
# # Pattern - Aggregate
# # Difficulty: ⭐☆☆☆☆

numbers = [8, -5, 10, 3, -2]

def sum_of_positive_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0 and number > 0:
            total += number
    return total

print(sum_of_positive_even_numbers(numbers))

# Problem 12 — Search + Validation
# Given numbers = [5, 8, -2, 9]. Write find_first_negative(numbers). Requirements: Return the first negative number. 
# Return None if none exists. Raise a ValueError if numbers is None.
# Pattern - Search
# Difficulty: ⭐☆☆☆☆

numbers = [5, 8, -2, 9]

def find_first_negative(numbers):
    if numbers is None:
        raise ValueError("numbers cannot be None.")
    
    for number in numbers:
        if number < 0:
            return number
    return None

print(find_first_negative(numbers))

# Problem 13: Count. Given scores = [82, 65, 91, 40, 88], return how many scores are 90 or above.
# Pattern - Count
# Difficulty: ⭐☆☆☆☆

scores = [82, 65, 91, 40, 88]

def scores_above_90(scores):
    count = 0
    for score in scores:
        if score >= 90:
            count += 1
    return count

print(scores_above_90(scores))

# Problem 14: Collect Given: names = ["Ada", "Christopher", "John", "Elizabeth"]. Return all names longer than five characters.
# Pattern: Collect
# Difficulty: ⭐☆☆☆☆

names = ["Ada", "Christopher", "John", "Elizabeth"]

def names_over_five_characters(names):
    result = []
    for name in names:
        if len(name) > 5:
            result.append(name)
    return result

print(names_over_five_characters(names))

# Problem 15 — Aggregate. Given: transactions = [200, -50, 300, -100, 150]. Return the sum of all positive transactions.
# Pattern: Aggregate
# Difficulty: ⭐☆☆☆☆

transactions = [200, -50, 300, -100, 150]

def sum_positive_transactions(transactions):
    total = 0
    for transaction in transactions:
        if transaction > 0:
            total += transaction
    return total

print(sum_positive_transactions(transactions))

# Problem 16 — Dictionary Lookup. Given: ages = {"Samson": 31, "Ada": 25, "John": 40}. Return Samson's age.
ages = {"Samson": 31, "Ada": 25, "John": 40}
print(ages["Samson"])

# Problem 17 — Dictionary Update. Given: inventory = {"apple": 10, "banana": 5}. Increase the number of apples to 15.
inventory = {"apple": 10, "banana": 5}
inventory["apple"] = 15
print(inventory)

# Problem #18 — Membership. Given: student = {"name": "Ada", "age": 22}. Determine whether "country" exists as a key. Return True or False.
student = {"name": "Ada", "age": 22}
if "country" in student:
    print(True)
else:
    print(False)

# Problem 19 — Frequency Count. Given: animals = ["dog", "cat", "dog", "bird", "cat", "dog"]. Return:{"dog": 3, "cat": 2, "bird": 1}
# Pattern: Frequency count
# Difficulty: ⭐☆☆☆☆

animals = ["dog", "cat", "dog", "bird", "cat", "dog"]

def count_of_animals(animals):
    frequency_count = {}
    for animal in animals:
        if animal in frequency_count:
            frequency_count[animal] += 1
        else:
            frequency_count[animal] = 1
    return frequency_count

print(count_of_animals(animals))

# Problem 20 — Most Common Word (Reasoning First) Given: words = ["python", "sql", "python", "ml", "sql", "python"]. Return the count of words
words = ["python", "sql", "python", "ml", "sql", "python"]

def frequency_of_words(words):
    frequency_count = {}
    for word in words:
        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1
    return frequency_count

print(frequency_of_words(words))

# Problem 21 — Remove Duplicates. Given: numbers = [5,8,3,8,5,1]. Return only the unique numbers.
numbers = [5,8,3,8,5,1]
print(set(numbers))

# Problem 22 — Membership. Given: employees = {"Ada", "John", "Samson"}. Return whether: "Mary" exists.
employees = {"Ada", "John", "Samson"}
print("Mary" in employees)

# Problem 23 — Find First Duplicate. Given: numbers = [4, 8, 3, 8, 5, 3]. Return: 8
numbers = [4, 8, 3, 8, 5, 3]

def unique_number(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None
print(unique_number(numbers))

# Problem 24 — Common Elements. Given: python = {"Ada", "John", "Samson"} sql = {"John", "Mary", "Samson"}. Return everyone who knows both.
python = {
    "Ada",
    "John",
    "Samson"
}

sql = {
    "John",
    "Mary",
    "Samson"
}
print(python & sql)

# Problem 25 — Difference. Return everyone who knows Python but not SQL.
print(python - sql)

# Problem 26 (Medium). Given words = ["cat", "dog", "cat", "bird", "dog", "dog"]. Find the most frequent word.
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
most_common = None
highest_count = 0

for word, count in freq.items():
    if count > highest_count:
        highest_count = count
        most_common = word
print(most_common)

# Problem 27 (Medium). Given text = "mississippi". Return the frequency of each character using the .get() pattern.
text = "mississippi"

freq = {}
for letter in text:
    freq[letter] = freq.get(letter, 0) + 1
print(freq)

# Problem 28 (Easy–Medium). Given numbers = [4, 8, 15, 16, 23, 42]. Build a dictionary where every number is a key and the value is True.
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

# Problem 29: Interview Style. Without using collections.Counter, determine whether two strings are anagrams. Example: "listen","silent" Output: True
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

# Exercise 30: Build a frequency dictionary for: word = "programming". Expected output:{'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}
word = "programming"

def freq_dict(word):
    freq = {}
    for letter in word:
            freq[letter] = freq.get(letter, 0) + 1
    return freq

print(freq_dict(word))

# Exercise 31: Write a function: same_frequency(word1, word2). It should return the two frequency dictionaries, 
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

# Exercise 32: Modify Exercise 8 so it returns: True. if the dictionaries are equal, otherwise False
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

# Exercise 33 – Count Numbers. Given: numbers = [1, 2, 2, 3, 1, 4, 2, 5]. Return:{1: 2, 2: 3, 3: 1, 4: 1, 5: 1}
numbers = [1, 2, 2, 3, 1, 4, 2, 5]

def count_number(numbers):
    freq = {}
    for number in numbers:
        freq[number] = freq.get(number, 0) + 1
    return freq

print(count_number(numbers))

# Exercise 34 – Count Characters. Given: text = "hello world" Count every character. Expected:{'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}
text = "hello world"

def count_characters(text):
    freq = {}
    for letter in text:
        freq[letter] = freq.get(letter, 0) + 1
    return freq

print(count_characters(text))

# Exercise 35 - Given: sentence = "python is fun python is awesome". Split the sentence into words and count each word. 
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

# Exercise 36 – Highest Score. Given: scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}. Return "David". Do not use max().
scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}

def highest_score(scores):
    for key, value in scores.items():
        if value > 91:
            return key
    return None
print(highest_score(scores))

# Exercise 37 – Lowest Score. Given: scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}. Return "Charlie". Do not use min().
scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}

def lowest_score(scores):
    for key, value in scores.items():
        if value < 80:
            return key
    return None
print(lowest_score(scores))

# Exercise 38 – Average Score. Given: scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}. Return the average score. Do not use sum().
scores = {"Alice":85, "Bob":91, "Charlie":78, "David":95}
# struggled with this. Repeat Later

def average_scores(scores):
    total = 0
    for score in scores.values():
        total += score
    average = total/len(scores)
    return average

print(average_scores(scores))

# Exercise 39: Frequency Pattern – First Repeated Number. Given numbers = [3,7,2,5,7,9], Return 7. 
# Hint: Use a dictionary. As soon as you see a number twice... Return it.
# struggled with this. Repeat Later
numbers = [3,7,2,5,7,9]

def repeated_number(numbers):
    seen = {}
    for number in numbers:
        if number in seen:
            return number
        seen[number] = True 
    return None
print(repeated_number(numbers)) 

# Exercise 40 – First Non-Repeated Number. Given numbers = [4,5,1,2,0,4,1,2] Return 5. Why? Because it appears exactly once.
# struggled with this. Repeat Later
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

# Exercise 41 – Duplicate Detection. Given numbers = [8,3,5,1,6,3], Return True because a duplicate exists.
# If numbers = [8,3,5,1]. Return False
# struggled with this. Repeat Later
numbers = [8,3,5,1,6,3]

def duplicate_detection(numbers):
    seen = {}
    for number in numbers:
        if number in seen:
            return True
        seen[number] = True
    return False

print(duplicate_detection(numbers))

# Exercise 42 – Count Even Numbers. Given numbers = [2,4,5,6,8,9,10], Return {2:1, 4:1, 6:1, 8:1, 10:1}. Ignore odd numbers.
# struggled with this. Repeat Later
numbers = [2,4,5,6,8,9,10]

def count_even_numbers(numbers):
    count = {}
    for number in numbers:
        if number % 2 == 0:
            count[number] = count.get(number, 0) + 1
    return count
        
print(count_even_numbers(numbers))