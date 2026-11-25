stu_info = {
    "name": "Ravi",
    "marks": [48, 78]
}

# Accessing & updating
print(stu_info["marks"][1])   # Output: 78
stu_info["marks"][1] = 90
print(stu_info["marks"][1])   # Output: 90

# Traversing (when all values are iterable)
for k, v in stu_info[1:].items():
    print(k)
    for mark in v[:]:
        print(mark)