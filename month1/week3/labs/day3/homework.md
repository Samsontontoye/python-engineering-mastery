# Homework Week 3 Day 3

1. What exception does each of the three snippets in Mini Exercise 1 raise?
# Mini Exercise 1: A (No Running)
int("python")
Answer: Raises a ValueError: invalid literal for int() with base 10: 'python'. Python knows what int() is supposed to do, but "python" cannot be converted into an integer.

# Mini Exercise 1: B (No Running)
numbers = [1, 2]
print(numbers[5]) 
Answer: IndexError: list index out of range. The index exists in the syntax but not in the list.

# Mini Exercise 1: C (No Running)
print(score) 
Answer: Results in a NameError: name 'score' is not defined. Python searches: Local scope, Global scope, Built-ins and cannot find score.

2. In Mini Exercise 2, should find_first_positive(None) return None or raise an exception? Why?
The function should raise an exception. It should raise an exception because there is a no list object that it can loop through to find the first positive number.
None usually means: Missing data, No value supplied, Programmer mistake

3. Why is catching specific exceptions generally better than writing a bare except:?
Catching specific exceptions is better because it makes debugging easier, prevents hiding unrelated bugs, and allows the program to handle only the errors it actually expects.

try and except are keywords used for exception handling, which is a mechanism to catch errors and prevent your program from crashing

A Helpful Rule of Thumb

When you're deciding between raise and assert, ask yourself:

Can a user or caller reasonably cause this? → Use raise (e.g., ValueError, TypeError).
Should this only happen if there's a bug in my code? → Use assert.