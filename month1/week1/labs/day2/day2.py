# Variables, Memory & Your First Real Python Program

name = "Samson"
age = 25
height = 1.82
is_engineer = True


print(type(age))
print(type(name))
print(type(height))
print(type(is_engineer))

name = input("What is your name? ")
print("Hello", name)

# f string
name = input("What is your name? ")
age = input("How old are you? ")
country = input("What country are you from? ")
print(f"Welcome {name}, you are {age} years old, and you live in {country}")

name = "Samson"
print(name)

first_name = "Sony"
last_name = "Ericsson"
age = 50
country = "Sweden"
profession = "engineer"

# exercise 1
print(first_name)
print(last_name)
print(age)
print(country)
print(profession)

# exercise 2
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(country))
print(type(profession))

# exercise 3
name = input("What is your name? ")
age = int(input("How old are you? "))
language = input("What is your favorite programming language? ")

print(f"My name is {name}, I am {age} years old and my favorite programming language is {language}")

# exercise 4
name = "Samson"
age = 23
country = "Nigeria"
profession = "Data Scientist/Machine Learning Engineer"

print(f"Hello Everyone, my name is {name}, i am {age} years old. I am from {country} and i work as a {profession}")