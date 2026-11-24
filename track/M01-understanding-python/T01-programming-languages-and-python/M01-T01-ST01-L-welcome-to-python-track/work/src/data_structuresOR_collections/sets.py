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

# union() - | operator also can be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.union(fruits2))

# intersection() - & operator also can be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.intersection(fruits2))

# difference()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.difference(fruits2))
print(fruits2 - fruits)

# symmetric_difference() - ^ operator also can be used
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.symmetric_difference(fruits2))
print(fruits ^ fruits2)

# update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.update(fruits2)
print(fruits)

# discard()

fruits.discard("apple")
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# difference_update()
fruits = {"apple", "banana", "kiwi", "grapes"}
fruits2 = {"orange", "mango", "grapes"}

fruits.difference_update(fruits2)
print(fruits)

# intersection_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.intersection_update(fruits2)
print(fruits)

# symmetric_difference_update()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

fruits.symmetric_difference_update(fruits2)
print(fruits)

# isdisjoint()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"orange", "mango", "grapes"}

print(fruits.isdisjoint(fruits2))


# issubset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"apple", "banana", "kiwi", "orange", "mango", "grapes"}

print(fruits.issubset(fruits2))

# issuperset()
fruits = {"apple", "banana", "kiwi"}
fruits2 = {"apple", "banana", "kiwi", "orange", "mango", "grapes"}

print(fruits.issuperset(fruits2))

# frozenset()
fruits = frozenset({"apple", "banana", "kiwi"})
print(fruits, type(fruits))

# Frozen set methods
# union()
fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})

print(fruits.union(fruits2))

# intersection()
fruits = frozenset({"apple", "banana", "kiwi"})
fruits2 = frozenset({"orange", "mango", "grapes"})