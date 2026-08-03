# Hash Maps + Frequency Counting Pattern
# Valid Anagram (NeetCode)
# Problem: Two strings are anagrams if they contain the same letters with the same frequencies.

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

print(is_anagram("eat", "tea"))
# The time and space complexity is O(n)

# Exercise 1: Build a frequency dictionary for: word = "banana"

word = "banana"

def frequency_counter(word):
    freq = {}
    for character in word:
        freq[character] = freq.get(character, 0) + 1
    return freq

print(frequency_counter(word))

# OR

def frequency_counter(word):
    freq = {}
    for character in word:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1
    return freq

print(frequency_counter(word))

# Exercise 2: Build a frequency dictionary for: numbers = [1, 2, 2, 3, 1, 4]
numbers = [1, 2, 2, 3, 1, 4]

def number_counter(numbers):
    freq = {}
    for number in numbers:
        freq[number] = freq.get(number, 0) + 1
    return freq

print(number_counter(numbers))

# OR
def number_counter(numbers):
    freq = {}
    for number in numbers:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
    return freq

print(number_counter(numbers))

# Exercise 3: Return the number of unique characters in: word = "mississippi"
word = "mississippi"

def character_counter(word):
    freq = {}

    for character in word:
        freq[character] = freq.get(character, 0) + 1

    return len(freq)

# OR
print(len(set(word)))

# Exercise 4 Medium: Write: most_frequent_letter(word). Example: most_frequent_letter("banana") Returns: "a". Do not use max().
word = "banana"

def most_frequent_letter(word):
    count = {}
    # count each letter
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # most frequent appearing letter
    most_frequent = None
    highest_count = 0

    for letter in count:
        if count[letter] > highest_count:
            highest_count = count[letter]
            most_frequent = letter
    return most_frequent
print(most_frequent_letter(word))

# Exercise 5 Write: least_frequent_letter(word). Do not use min().
word = "banana"

def least_frequent_letter(word):
    count = {}
    # count each letter
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    # least frequent occuring letter
    least_letter = None
    least_count = float("inf")

    for letter in count:
        if count[letter] <= least_count:
            least_count = count[letter]
            least_frequent = letter
    return least_frequent

print(least_frequent_letter(word))

# Exercise 6 Write: same_frequency(word1, word2). Return the two frequency dictionaries without comparing them. 
# Example: same_frequency("cat", "tac") Returns: ({"c": 1, "a": 1, "t": 1}, {"t": 1, "a": 1, "c": 1})

def same_frequency(word1, word2):
    count1 = {}
    count2 = {}

    for letter in word1:
        if letter in count1:
            count1[letter] += 1
        else:
            count1[letter] = 1
    
    for letter in word2:
        if letter in count2:
            count2[letter] += 1
        else:
            count2[letter] = 1
    
    return count1, count2

print(same_frequency("cat", "tac"))

# Exercise 7: Pattern Building: Modify Exercise 6. Now return True if the dictionaries are equal.
# Otherwise False. This is essentially the Valid Anagram solution.
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

# OR

def same_frequency(word1, word2):
    if len(word1) != len(word2):
        return False
    
    freq1 = {}
    freq2 = {}

    for letter in word1:
        if letter in freq1:
            freq1[letter] += 1
        else:
            freq1[letter] = 1

    for letter in word2:
        if letter in freq2:
            freq2[letter] += 1
        else:
            freq2[letter] = 1

    return freq1 == freq2
print(same_frequency("cat", "tac"))

# Exercise 8 Given: words = ["apple", "banana", "apple", "orange", "banana", "apple"]. Return the most frequent word.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def most_frequent_word(words):
    freq = {}
    # count each word
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # find the most frequent word
    highest_count = 0
    most_common = None

    for word, count in freq.items():
        if count > highest_count:
            highest_count = count
            most_common = word
    return freq, highest_count

print(most_frequent_word(words))

# Exercise 9 Guided Challenge. Given: list1 = [1, 2, 2, 3], list2 = [2, 3, 2, 1] Return: True
# if both lists contain the same values with the same frequencies.

list1 = [1, 2, 2, 3] 
list2 = [2, 3, 2, 1]

def list_frequency(list1, list2):
    if len(list1) != len(list2):
        return False
    
    freq1 = {}
    freq2 = {}

    for number in list1:
            freq1[number] = freq1.get(number, 0) + 1

    for number in list2:
        freq2[number] = freq2.get(number, 0) + 1

    return freq1 == freq2

print(list_frequency(list1, list2)) 

# Exercise 10 Stretch Challenge. Write a function: build_frequency(data) It should work for:
# build_frequency("banana") and build_frequency([1, 2, 2, 3]) without changing the function.

def build_frequency(data):
    freq = {}

    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(build_frequency([1, 2, 2, 3]))

# OR

def build_frequency(data):
    freq = {}

    for item in data:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

print(build_frequency("banana"))