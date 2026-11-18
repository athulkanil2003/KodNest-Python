# Tuples -> () ordered, immutable, heterogeneous data

nums = (1, 2, 3, 4)
# nums[0] = 100 # immutable
print(nums, type(nums))

#index        0           1     2     3
stu_info = ("Mohammad", True, 7.93, 22)
print(stu_info)
print(stu_info[3]) # indexing
print(stu_info[0:3]) # slicing
print(stu_info[-2]) # negative indexing

name = ("Gamana",) * 3
print(name)
print(type(name)) # check the type of the variable

# Tuple Constructor
lst = [1, 2, 3]
print(lst, type(lst))
rgb = tuple(lst)
print(rgb)
print(type(rgb)) # check the type of the variable

rgb = tuple(["r", "e", "d"])
print(rgb)
print(type(rgb)) # check the type of the variable

# Adding and removing elements
x = (1, 2, 3)
z = (10, 11, 12)
# z.pop()
# del z will give error
print(z)
x += z # x = x + z
print(x)
y = list(x)
y.append(4)
print(y)

# loop
z = (10, 11, 12, 10)
for i in range(len(z)):
    print(z[i])
# methods in tuples
print(z.count(10)) # 2
print(z.index(10)) # 0
print(z.index(10, 2)) # 3

# Unpacking of tuples
emp = ("Mohammad", 22, "Developer")
print(emp, type(emp))
(name, age, role) = emp # Unpack
print(name)
print(age)
print(role)

# TUPLE *
s = (2, 4, 6, 8, 10)
(a, *b, c) = s
print(a)
print(b)
print(c)

# Other methods
t = (10, 20, 30, 40, 50)

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(any(t))
print(all(t))
print(10 in t)

t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)
print(t1 * 2)

del t