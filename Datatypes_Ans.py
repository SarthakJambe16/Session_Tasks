#1
a = [1, 2, 2, 3, 4, 4, 5]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)

#2
a = [10, 20, 30, 40, 50]

first = 0
second = 0

for i in a:
    if i > first:
        second = first
        first = i

print(second)

#3
a = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)

#4
a = [1, 2, 2, 3, 3, 3]
b = []

for i in a:
    if i not in b:
        count = 0

        for j in a:
            if i == j:
                count = count + 1

        print(i, count)
        b.append(i)
        
#5
a = [0, 1, 0, 3, 12]
b = []

for i in a:
    if i != 0:
        b.append(i)

for i in a:
    if i == 0:
        b.append(i)

print(b)

#6
a = (1, 2, 3, 4, 5)
b = ()

for i in a:
    b = (i,) + b

print(b)

#7
a = (10, 20, 5, 40, 15)

big = a[0]
small = a[0]

for i in a:
    if i > big:
        big = i
    if i < small:
        small = i

print(big)
print(small)

#8
a = (10, 20, 10, 30, 10, 40)

num = 10
count = 0

for i in a:
    if i == num:
        count = count + 1

print(count)

#9
a = (10, 20, 10, 30, 20)

b = list(a)

c = []

for i in b:
    if i not in c:
        c.append(i)

d = tuple(c)

print(d)

#10 
students = (("Amit", 85), ("Rahul", 92), ("Sneha", 78), ("Priya", 95))

name = ""
marks = 0

for i in students:
    if i[1] > marks:
        marks = i[1]
        name = i[0]

print(name)
print(marks)

#11
a = [10, 20, 30, 40]
b = [20, 40, 50, 60]

x = set(a)
y = set(b)

print(x & y)

#12
a = [10, 20, 30]
b = [20, 30, 40]

c = set(a + b)

print(c)

#13
a = {10, 20}
b = {10, 20, 30, 40}

for i in a:
    if i not in b:
        print("Not Subset")
        break
else:
    print("Subset")
 
#14
a = {10, 20, 30, 40}
b = {20, 30, 50, 60}

for i in b:
    if i in a:
        a.remove(i)

print(a)
print(b)

#15
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

c = set()

for i in a:
    if i not in b:
        c.add(i)

for i in b:
    if i not in a:
        c.add(i)

print(c)

#16
a = "programming"
d = {}

for i in a:
    d[i] = a.count(i)

print(d)

#17
a = "python is easy and python is powerful"
b = a.split()
d = {}

for i in b:
    d[i] = b.count(i)

print(d)

#18
students = {"Amit": 85, "Rahul": 92, "Sneha": 78, "Priya": 95}

marks = 0
name = ""

for i in students:
    if students[i] > marks:
        marks = students[i]
        name = i

print("Student:", name)
print("Marks:", marks)

#19
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}

d = d1.copy()

for i in d2:
    if i in d:
        d[i] = d[i] + d2[i]
    else:
        d[i] = d2[i]

print(d)

#20
d = {"a": 30, "b": 10, "c": 20}

a = list(d.items())

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i][1] > a[j][1]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(dict(a))