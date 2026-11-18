# set - {}, unordered, unindexed,
# mutable(items are unchangeable but add or remove), no duplicates

fruits = {"apple", "banana", "kiwi", "apple"}
print(fruits, type(fruits))

# set constructor
stu_info = set(("RAm", 23, 89.65, "a"))
print(stu_info, type(stu_info), len(stu_info))

fruits2 = set(("apple", "banana", "kiwi"))
print(fruits2, type(fruits2))

# set methods
# add()
fruits = {"apple", "banana", "kiwi", "apple"}
nfruits = {"orange", "lemon", "grapes"}
fruits.update(nfruits)
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# discard()
fruits.discard("apple")
print(fruits)

# pop() - last element removed
fruits.pop()
print(fruits)

# clear()
fruits.clear()
print(fruits)

# del
del fruits
# print(fruits)

fruits = {"apple", "banana", "kiwi"}
for i in fruits:
    print(i)

# Immutable frozenset
fruits = frozenset({"apple", "banana", "kiwi"})
print(fruits, type(fruits))
for i in fruits:
    print(i)
#fruits.add("orange")
print(fruits)