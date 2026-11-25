marks = [[45, 75], [48, 78]]

# Accessing & updating
print(marks[1][1])   # Output: 78
marks[1][1] = 90
print(marks[1][1])   # Output: 90

# Traversing
for mark in marks:
    for m in mark:
        print(m,end=" ")