# Loops — Processing Data One Element at a Time

numbers = [3, 8, 2, 9]

for number in numbers:
    print(number)

for i in range(5):
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1

ids = [101, 202, 303, 404]

for customer_id in ids:
    if customer_id == 404:
        print("Found")
        break

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# Exercise 1
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(fruit)

# exercise 2
for i in range(1, 11):
    print(i)

# Exercise 3
numbers = [5, 10, 15, 20]

total = 0

for number in numbers:
    total += number

print(total)

# exercise 4
numbers = [1,2,3,4,5,6,7,8]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# exercise 5 Use a while loop to count down from: 5 to 1 Then print: Blast Off!

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Blast Off!")

# interview problem: given the number, Return the first even number. Return None if no even number exists. Stop searching as soon as you find the answer.
# solution 
numbers = [4, 7, 2, 9, 6, 8]

def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None

print(find_first_even(numbers))

# total = 0

# for i in [5, 10, 15]:
#     total = total + i

# print(total)