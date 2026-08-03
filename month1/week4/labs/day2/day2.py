# Sets & Hashing (The Foundation of Fast Lookups)
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)
numbers.remove(2)
print(numbers)
numbers.discard(100)
print(numbers)
print(5 in numbers)
print(len(numbers))

# Example 1: Contains Duplicate. Problem: Given an integer array, return True if any value appears at least twice.
# Otherwise return False. Example 1 [1,2,3,1] Return True
numbers = [1, 2, 3, 1]

def contains_duplicate(numbers):
    # seen = {}
    # for number in numbers:
    #     if number in seen:
    #         return True
    #     seen[number] = True
    # return False
        
# OR
      seen = set()
      for number in numbers:
            if number in seen:
                  return True
            seen.add(number)
      return False

print(contains_duplicate(numbers))

# Exercise 2: Create a set from: numbers = [1,2,2,3,4,4,5]. Print the result.
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))

# Exercise 3: Add 10 to: numbers = {2,4,6}. Then remove 4.
numbers = {2, 4, 6}
numbers.add(10) # Time complexity is O(1) average since we aren't looping
numbers.remove(4) # Time complexity is O(1) average since we aren't looping
print(numbers)

# Rule to Remember: Whenever you see .add(), .remove(), .discard(), .pop() on a set, think
# Constant time (O(1) average) unless you're doing them inside a loop, then it becomes O(n).

# Exercise 4 - Check whether 7 exists in {3,5,7,9} without using a loop.
numbers = {3,5,7,9}
print(7 in numbers) # # Time complexity is O(1) average since we aren't looping

# Exercise 5 - Write a function: remove_duplicates(numbers). Example: [1,2,2,3,3,4] returns [1,2,3,4]
numbers = [1,2,2,3,3,4]

def remove_duplicates(numbers):
      result = set()
      for number in numbers:
                result.add(number)
      return result
                     
print(remove_duplicates(numbers))

# Exercise 6 - Count how many unique words are in: words = ["python", "java", "python", "c++", "java", "go"]
words = ["python", "java", "python", "c++", "java", "go"]
print(len(set(words))) # This returns 4 as the number of unique words

def unique_words(words):
     count = {}
     for word in words:
          count[word] = count.get(word, 0) + 1
     return count
print(unique_words(words))

# OR
def unique_words(words):
       count = {}
       for word in words:
              if word in count:
                     count[word] += 1
              else:
                     count[word] = 1
       return count
print(unique_words(words))

# Exercise 7: Write a function: has_duplicate(numbers) and it should return True or False using a set.
numbers = [1,2,2,3,3,4]

def has_duplicates(numbers):
      result = set()
      for number in numbers:
            if number in result:
                  return True
            result.add(number)
      return False
print(has_duplicates(numbers))

# Exercise 8. Given: list1 = [1,2,3,4], list2 = [3,4,5,6]. Return all values that appear in both lists. Hint: Convert one list to a set first.
list1 = [1,2,3,4]
list2 = [3,4,5,6]

set1 = set(list1)
set2 = set(list2)

print(set1 & set2)
# Time complexity
# Creating set1 and set2 requires storing all elements. Space: O(n + m) where n = size of list1, m = size of list2

list1 = [1,2,3,4]
list2 = [3,4,5,6]

def set_values(list1, list2):
      set1 = set(list1)
      set2 = set(list2)
      for number in set1, set2:
            return set1 & set2
            
print(set_values(list1, list2))

# Exercise 9 - Given: numbers = [4,7,2,9,1]. Return True if 7 exists. Solve it using a set.
numbers = [4,7,2,9,1]

def if_7_exsists(numbers):
      return 7 in numbers

print(if_7_exsists(numbers))

# OR

print(7 in numbers)

# OR

def contains_seven(numbers):
    lookup = set(numbers)
    return 7 in lookup

# Exercise 10 - Write a function: first_duplicate(numbers) Example: [2,5,1,3,5,7] returns 5
numbers = [2,5,1,3,5,7]

def first_duplicate_numbers(numbers):
      seen = {}
      for number in numbers:
            if number in seen:
                  return number
            seen[number] = True
      return None
      
print(first_duplicate_numbers(numbers))

# OR

def first_duplicate_numbers(numbers):
      seen = set()
      for number in numbers:
            if number in seen:
                  return number
            seen.add(number)
      return None
      
print(first_duplicate_numbers(numbers))

# Exercise 11 - Without using nested loops, determine whether two lists share at least one common element.
# Example: [1,2,3] and [7,8,2] Return: True
      
list1 = [1, 2, 3]
list2 = [7, 8, 2]

set1 = set(list1)
set2 = set(list2)

print(set1 & set2)