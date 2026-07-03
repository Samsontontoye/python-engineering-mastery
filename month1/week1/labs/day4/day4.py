# LISTS

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

numbers = [10, 20, 30]
numbers[0] = 99
print(numbers)

languages = ["Python", "SQL", "Java"]
# print(languages)
# print(languages[0])
# print(languages[2])
# print(languages[1])

languages.remove("Java")
languages.insert(2, "GO")
print(languages)

languages.append("Rust")
print(languages)

languages.pop(1)
print(languages)

# Print the largest number. Rules:
# Don't use max().
# Don't sort the list.
# Solve it yourself.

numbers = []

# assume the first number is the largest
largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num
print(largest)

numbers = [8, 2, 10, 5, 7]

largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num

print(num)
print(largest)

numbers = [8, 2, 10, 5, 7]

largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num

num = 100

print(num)
print(largest)

a = [1, 2, 3]

b = a

b = [4, 5, 6]

print(a)
print(b)

