#1
numbers = [10, 20, 10, 30, 20, 40]
unique_numbers = []
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(unique_numbers)

#2
numbers = [10, 50, 20, 80, 40]
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest number:", second)

#3
numbers = [10, 15, 20, 25, 30, 35]
even_numbers = []
odd_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)

#4
list_1 = [10, 20, 30, 40]
list_2 = [30, 40, 50, 60]
common = []
for item in list_1:
    if item in list_2 and item not in common:
        common.append(item)
print(common)

#5 
numbers = [0, 10, 0, 20, 30, 0, 40]
without_zeros = []
zero_count = 0
for i in numbers:
    if i == 0:
        zero_count += 1
    else:
        without_zeros.append(i)
result = without_zeros + [0] * zero_count
print(result)

#6
numbers = [10, 20, 10, 30, 20, 40]
unique_values = set(numbers)
print(unique_values)

#7
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A | B)
print(A & B)

#8
A = {10, 20, 30, 40}
B = {30, 40, 50}
print(A - B)

#9
java_students = {"Amit", "Rahul", "Sneha", "Priya"}
python_students = {"Sneha", "Priya", "Raj", "Kiran"}
print(java_students & python_students)

#10
A = {10, 20}
B = {10, 20, 30, 40, 50}
if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

#11
values = (45, 12, 89, 23, 67)
maximum = minimum = values[0]
for value in values[1:]:
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value
print(maximum)
print(minimum)

# 12. Count occurrences without using count().
values = (10, 20, 10, 30, 10, 40)
target = 10
frequency = 0
for i in values:
    if i == target:
        frequency += 1
print(f"{target} occurs {frequency} times")

#13
values = (10, 20, 30, 40, 50)
reversed_values = values[::-1]
print(reversed_values)

#14
values = (10, 20, 10, 30, 20, 40, 50)
seen = []
duplicates = []
for i in values:
    if i in seen:
        if i not in duplicates:
            duplicates.append(i)
    else:
        seen.append(i)
print(tuple(duplicates))

#15
T1 = (10, 20, 30, 40)
T2 = (30, 40, 50, 60)
common_values = []
for value in T1:
    if value in T2 and value not in common_values:
        common_values.append(value)
print(tuple(common_values))
