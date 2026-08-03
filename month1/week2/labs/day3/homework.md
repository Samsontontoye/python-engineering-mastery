# Homework Week 2 Day 3

## Question 1
What is an accumulator?
Answer: An accumulator is a variable that stores a result as you iterate through a collection. It "accumulates" information over time.

Counting accumulator: keeps a running total. For example
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1

Collection accumulator: builds a new list.
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

# Question 2
Why create a new list instead of modifying the original?
Answer: Creating a new list is safer because:
- It preserves the original data.
- It avoids unexpected bugs.
- It makes your code easier to understand.
- It prevents problems that occur when changing a list while looping through it.

numbers = [1, 2, 3, 4]

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(numbers)  # [1, 2, 3, 4]
print(evens)    # [2, 4]

# Question 3
What does `append()` do?
Answer: append() adds a single item to the end of a list.
fruits = ["apple", "banana"]

fruits.append("orange")

print(fruits)
# ['apple', 'banana', 'orange']

# Question 4
When would you collect instead of count?
Answer: Use collect when you need the actual items later, not just how many there are.

Examples:

Find all even numbers.
Get all customers with overdue loans.
Extract all email addresses.
Build a filtered dataset.

Use count when you only care about the number.

# Count
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1

# Collect
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

# Question 5
Why can modifying a list while iterating over it be dangerous?
Answer: Changing the list (adding or removing elements) while looping over it changes its size and positions, which can cause elements to be skipped or processed incorrectly.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)
output: [1, 3, 5]