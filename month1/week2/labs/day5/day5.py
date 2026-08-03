# Dictionaries — Python's Most Important Data Structure
person = {
    "name": "Samson",
    "age": 25,
    "profession": "Data Scientist"
}

print(person["name"])
print(person.get("name"))
print(person["age"])
print(person["profession"])

# adding new keys
person["country"] = "Nigeria"

# Updating Values
person["age"] = 26
print(person)

# Exercise 1: Create a dictionary describing yourself.
# Include: name, age, profession, country. Print each value.
person = {
    "name": "Samson",
    "age": 25,
    "profession": "Data Scientist",
    "country": "Nigeria"
}

print(person["name"])
print(person["age"])
print(person["profession"])
print(person["country"])

# Exercise 2: Update your profession. Print the dictionary.
person.update({"profession": "machine learning engineer"})
print(person)

# Exercise 3: Add: favorite_language. Print the dictionary.
person.update({"favorite_language": "ijaw"})
print(person)

# Exercise 4. Remove one key. Print the result.
person.pop("country")
print(person)

# exercise 5: Loop through the dictionary. Print: key : value. Example name : Samson, age : 25
for key, value in person.items():
    print(key, value)

# interview problem: Given the word below, Write count_words(words) and Return

# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]

def count_word(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_word(words))

person = {}

person["name"] = "Samson"
person["age"] = 25

print(person["country"])

person = {
    "name": "Samson"
}

print(person.get("age"))

print(person["age"])

# given
customers = [
    {"name": "Ada", "country": "Nigeria"},
    {"name": "John", "country": "Kenya"},
    {"name": "Grace", "country": "Nigeria"},
    {"name": "Paul", "country": "Ghana"},
]


# Write a function that returns:

# {
#     "Nigeria": 2,
#     "Kenya": 1,
#     "Ghana": 1
# }
# This is an example of frequency count

def country_count(customer):
    country_counts = {}
    for customer in customers:
        country = customer["country"]
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    return country_counts

print(country_count(customers))
