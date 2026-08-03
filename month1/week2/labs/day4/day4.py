# Tuples & Sets — Choosing the Right Data Structure
person = ("Samson", 20, "Nigeria")
# person[0] = "John" results in a type error cos tuples are immutable
print(person[0])

# tuple unpacking
person = ("Samson", 20, "Nigeria")
name, age, country = person
print(person)

# set
# What Makes Sets Special? Sets have two defining characteristics.
# No duplicates. Example, the below set results in {1, 2, 3}
numbers = {1, 2, 2, 3, 3, 3}
numbers.add(4)
numbers.remove(2)
print(numbers)

# exercise 1: Create a tuple containing: your name, your age, your profession
person = ("Samson", 25, "Data Scientist")
name, age, profession = person
print(name)
print(age)
print(profession)

# Exercise 2: Try changing one element. Observe the error. Write down: Why does Python raise that error?
person[0] = "Emeka"
print(person) # results in a TypeError: 'tuple' object does not support item assignment cos tuples are immutable

# Exercise 3
numbers = {1,2,3,2,1,5}
numbers.add(10)
numbers.remove(2)
print(numbers)

# interview problem: Given the list below, write a function that removes duplicates and returns [2,5,7,8,9]. Don't use set().
numbers = [2,5,2,7,5,8,2,9]

def remove_duplicates(numbers):
    unique_values = []
    for number in numbers:
        if number not in unique_values:
            unique_values.append(number)
    return unique_values
        
print(remove_duplicates(numbers))

numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(2)
numbers.append(3)

print(numbers)