# Homework Week 2 Day 5

# Question 1
What is a dictionary?
Answer: A dictionary is a datatype for mutable object that stores mappings of unique keys to values. A dictionary is a collection of key-value pairs.

Think of it like a real dictionary:

You look up a word (the key).
You get its definition (the value).

# Question 2
What is a key?
Answer: A key is the identifier you use to look up information. Keys must be unique.

# Question 3
What is a value?
Answer: A value is the information associated with a key.

# Question 4
What's the difference between [] and .get()?
"person["age"] is appropriate when the key is required. Raising a KeyError helps detect bugs early if the expected data is missing. person.get("age") is appropriate when the key is optional, because it allows the program to continue by returning None or a default value instead of raising an exception."

person.get("age") says: "If the key exists, give it to me. Otherwise, return None (or a default value)."
person["age"] says: "This key must exist. If it doesn't, that's an error."

person["age"] is like saying, "Open the 'Age' folder." If the folder doesn't exist, someone stops you with an error.
person.get("age") is like asking, "Do we have an 'Age' folder?" If not, you're simply told, "No, we don't."

[] is strict and raises a KeyError for missing keys, while .get() is forgiving and returns None (or a default value) instead.

Answer: Suppose we have:

student = {
    "name": "Alice",
    "age": 25
}
Using []
print(student["name"])

Output: Alice

But if the key doesn't exist:

print(student["grade"])

Python raises an error:

KeyError: 'grade'

# Using .get()
print(student.get("name"))

Output: Alice

If the key doesn't exist:

print(student.get("grade"))

Output: None

No error.

You can even specify a default value:

print(student.get("grade", "Not Found"))

Output: Not Found

# Question 5
When would you use a dictionary instead of a list?
Answer: Use a list when the position of items matters. 

Use [] when the key is guaranteed to exist.
Use .get() when the key might be missing and you want to avoid a KeyError.

fruits = ["apple", "banana", "orange"]

To get "banana": fruits[1]

You're accessing it by index.
Real-world examples

Use a list when storing:

- Shopping items
- Test scores
- Daily temperatures
- Names in order
scores = [85, 90, 78, 95]

Use a dictionary when each item has a name (key).
Example:

student = {
    "name": "Alice",
    "age": 25,
    "city": "Lagos"
}

You access information by key:

student["age"]
Output: 25

Use a dictionary when storing:

User profiles
Product information
Employee records
Configuration settings

Example:

employee = {
    "id": 101,
    "name": "Samson",
    "department": "Data Science",
    "salary": 250000
}