# Homework Week 2 Day 4

# Question 1
What is a tuple?
Answer: A tuple is an ordered collection of items, similar to a list, but it cannot be changed after it is created (it is immutable).
coordinates = (10, 20)

print(coordinates[0])  # 10
Tuples use parentheses (), while lists use square brackets [].

# Question 2
Why are tuples immutable?
Answer: Tuples are immutable to ensure their contents remain constant. This provides several benefits:

- Prevents accidental modification.
- Makes code more predictable.
- Allows tuples to be used as dictionary keys (lists cannot).
- Can be slightly more memory-efficient than lists.

point = (3, 5)

point[0] = 10
This raises a TypeError because tuples cannot be modified.

# Question 3
What is a set?
Answer: A set is an immutable unordered collection of unique items.

fruits = {"apple", "banana", "orange"}

print(fruits)
Sets are useful when you only care whether an item exists and don't want duplicates.

# Question 4
Why don't sets allow duplicates?
Answer: A set represents a collection of unique values. If duplicates were allowed, it wouldn't serve its purpose.
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
output: {1, 2, 3}
Python automatically removes duplicate values when creating or updating a set.

# Question 5
When would you choose a tuple over a list?
Answer: Choose a tuple when the data should never change.

Examples:

Coordinates: (40.7128, -74.0060)
RGB color: (255, 0, 0)
Date: (2026, 7, 10)
Database record returned from a query
Dictionary keys (when multiple values form the key)
Choose a list when you'll need to add, remove, or modify items.

# Tuple (fixed data)
dimensions = (1920, 1080)

# List (modifiable data)
shopping_list = ["milk", "bread"]
shopping_list.append("eggs")