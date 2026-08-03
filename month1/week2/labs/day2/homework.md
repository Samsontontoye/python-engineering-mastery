# Homework Week 2 Day 2

## Question 1
What is a loop?
Answer: A loop is a programming construct that repeatedly executes a block of code until a condition is met or until it has processed all items in a collection.
for i in range(3):
    print(i)
output: 0, 1, 2

# Question 2
What is the difference between `for` and `while`?
Answer: A for loop is used when you know how many times to iterate or you're looping through a collection. A for loop Iterates over a sequence (list, string, range, etc.).
A while loop is used when you don't know in advance how many times you'll loop. A while loop repeats as long as a condition is True.

# for loop
for fruit in ["apple", "banana", "orange"]:
    print(fruit)

# while loop
count = 0

while count < 3:
    print(count)
    count += 1

# Question 3
What does `range(5)` produce?
Answer: 0, 1, 2, 3, 4

for i in range(5):
    print(i)

# Question 4
What does `break` do?
Answer: break immediately stops the loop and exits it, even if there are more iterations remaining.

for num in range(10):
    if num == 5:
        break
    print(num)
output: 0, 1, 2, 3, 4

# Question 5
What does `continue` do?
Answer: continue skips the rest of the current iteration and moves directly to the next one.

for num in range(5):
    if num == 2:
        continue
    print(num)
output: 0, 1, 3, 4