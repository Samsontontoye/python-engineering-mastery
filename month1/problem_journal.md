The Four Questions I Want in Your Head Forever

Whenever you see a problem, immediately ask:

Question 1

What pattern is this?

Question 2

What state do I need?

Question 3

When does that state change?

Question 4

Can I stop early?

For every problem you solve, don't just save the code.

Write this:

## Problem 1 — Sum Positive Numbers
# Sum Positive Numbers
# Difficulty: ⭐☆☆☆☆
# Pattern Focus: Aggregate
# problem 1: Given numbers = [3, 8, -2, 12, -5, 7], write a function sum_positive(numbers) that returns the total 30.
numbers = [3, 8, -2, 12, -5, 7]

def sum_positive(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

print(sum_positive(numbers)) # result = 30

Pattern:
Aggregate

Difficulty:
2/10

State:
total = 0

Biggest Lesson:
Aggregate problems require a running total.

Mistake I Made:
Initially misunderstood some edge cases like the empty list (sum_positive([]) should return 0) and lists with only negative numbers
([-5, -2, -10] should return 0 also).

Could I solve this again tomorrow without help?
Yes.

# Problem 2: Collect Long Words
# Collect Long Words
# Difficulty: ⭐☆☆☆☆
# Pattern Focus: Collect

# Problem 2: Given: words = ["apple", "hi", "banana", "go", "orange"]. Write: collect_long_words(words)
# and return ["apple", "banana", "orange"]. A long word is any word with more than 4 characters.

words = ["apple", "hi", "banana", "go", "orange"]

def collect_long_words(words):
    result = []
    for word in words:
        if len(word) > 4:
            result.append(word)
    return result
print(collect_long_words(words))

Pattern:
Collect

Difficulty:
2/10

State:
result = []

Biggest Lesson:
Collect problems needs an empty list to start with

Mistake I Made:
None

Could I solve this again tomorrow without help?
Yes.

# Problem 3: Given scores = [45, 82, 91, 67, 55, 100], count the high scores and return the count. write count_high_scores(scores) and return 3
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

Pattern:
Count

Difficulty:
2/10

State:
count = 0

Biggest Lesson:
Increase the count for everytime a high score is detected

Mistake I Made:
None

Could I solve this again tomorrow without help?
Yes.

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

Pattern:
Collect

Difficulty:
2/10

State:
result = []

Biggest Lesson:
Collect problems needs an empty list to start with

Mistake I Made:
None

Could I solve this again tomorrow without help?
Yes.