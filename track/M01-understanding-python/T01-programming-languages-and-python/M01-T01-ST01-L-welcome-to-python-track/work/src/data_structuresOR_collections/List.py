# Lists are mutable, ordered, and allow duplicate values and can be accessed using index, []
#index 0 1 2345
nums = [1, 2, 3,4, 5, 3]
print(nums)
print(nums [2])
print(type(nums)) # I

names = ["Alice", "Bob", "Charlie"]
names [1] = "David"
# names[3] = "Alice"
print(names)
print(type(names))

# List methods
names = ["Alice", "Bob", "Charlie"]
print(names)
names.append ("Ram")
print(names)
names.insert(2, "Sita")
print(names)
names.pop()
print(names)
names.remove("Sita")
print(names)
names.clear()
print(names)
del names
print(names)