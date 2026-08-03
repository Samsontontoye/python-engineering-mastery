# Topic: Dictionaries & Hash Maps
ages = {
    "Samson": 31,
    "Ada": 25,
    "John": 40
}

print(ages["Samson"])

# Think of a dictionary as a real-world dictionary. You don't read every page to find: "Python" You go directly to: "Python"
# and retrieve its definition. Programming dictionaries work the same way.

# Why are dictionaries generally much faster than searching through a list to find a value?
# Lists search by checking elements one after another (linear search, O(n)).
# Dictionaries use hash tables, allowing Python to jump directly to the correct key (average O(1)).
# This is why dictionaries are the preferred data structure when you need fast lookups by key, 
# while lists are better when the order of items matters or you frequently iterate through all elements.

student = {
    "name": "Samson",
    "age": 31,
    "country": "Nigeria"
}
print(student.keys())
print(student.values())

# Accessing Values
print(student["name"])

# updating
student["age"] = 25
print(student)
# The dictionary becomes
# {
#     "name": "Samson",
#     "age": 25,
#     "country": "Nigeria"
# }

# adding
student["career"] = "Data Scientist"
print(student)
# Now becomes
# {
#     "name": "Samson",
#     "age": 32,
#     "country": "Nigeria",
#     "job": "Data Scientist"
# }

book = {
    "title": "Deep Learning",
    "author": "Goodfellow",
    "pages": 775
}

book["pages"] = 80
book["price"] = 50
print(book)

# Why .get() Exists. Consider:
student = {
    "name": "Samson"
}
# Now
student["age"] # raises a KeyError because "age" doesn't exist.

# instead
student.get("age") # returns None and no exceptions

# Even better:
student.get("age", 0) # returns 0 if "age" is missing.

# When should you use:
student["age"]
# versus
student.get("age")

# Use [] when the key must exist. 
# Use .get() when the key is optional.

# Membership. Instead of
if student.get("age") is not None:

# you can write
if "age" in student: # This checks if the key exists.

# iterating: Keys
for key in student:
    print(key) # Output: name, age, country

# iterating: Values
for value in student.values():
    print(value)

# iterating: Both Key and value
for key, value in student.items():
    print(key, value) # name Samson, age 31, country Nigeria

# frequency counting
letters = [
    "a",
    "b",
    "a",
    "c",
    "a",
    "b"
]

def frequency_counting(letters):
    frequency = {}
    for letter in letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency

print(frequency_counting(letters)) 

# result
# {
#     "a": 3,
#     "b": 2,
#     "c": 1
# }

colors = [
    "red",
    "blue",
    "red",
    "green",
    "blue",
    "red"
]

def color_count(colors):
    frequency = {}
    for color in colors:
        if color in frequency:
            frequency[color] += 1
        else:
            frequency[color] = 1
    return frequency

print(color_count(colors)) # result: {'red': 3, 'blue': 2, 'green': 1}

# What pattern is this?: The pattern is frequency counting pattern
# What is the state? The state is frequency = {}
# What should the final dictionary look like?: The final dictionary should be 'red': 3, 'blue': 2, 'green': 1}

