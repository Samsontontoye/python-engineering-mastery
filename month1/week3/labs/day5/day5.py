# # Topic: Sets & Fast Membership Testing
numbers = [5, 8, 3, 8, 2, 5, 1]
unique_members = set(numbers)
print(unique_members)

# Creating Sets
# Empty set:
my_set = set()

# This is not a set:
my_set = {} # This creates a dict, not a set

# Adding
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.add("apple") # Nothing happens. Sets ignore duplicates.
print(fruits)

# Removing
fruits.remove("banana")
print(fruits)

# Membership Testing
numbers = [1,2,3,4,5,6,7,8,9]
print(9 in numbers) # True. This requires searching the list.

numbers = {1,2,3,4,5,6,7,8,9}
print(9 in numbers)

# Set Operations: Union
python = {
    "Samson",
    "Ada",
    "John"
}

sql = {
    "John",
    "Ada",
    "Mary"
}
print(python | sql) # | means union
# This returns {'Ada', 'Mary', 'John', 'Samson'} as the result

# Set Operations: Intersection
print(python & sql) # & means intersection

# Set Operations: Difference
print(python - sql) # - means difference

# Mini Exercise 1
numbers = [5,5,8,3,3,8,1]
unique = set(numbers)
print(unique)

# Mini Exercise 2
fruits = {"apple","banana"}
fruits.add("banana")
print(fruits)

# Mini exercise 3
fruits = {"apple"}
fruits.remove("banana")
print(fruits) # KeyError: 'banana'