#-------------------map-------------------
numbers = [1, 2, 3, 4, 5]
squares = []
for x in numbers:
    squares.append(x * 2)
print(squares)
#-----------------------------------------
def square(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print(squares)
#-----------------------------------------
numbers = [1, 2, 3, 4, 5]
#lambda parameter : body(operation) - lambda num : num * num
squares = list(map(lambda x: x * 2, numbers))
print(squares)
#-------------------filter-------------------
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)
print(evens)
#-----------------------------------------
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
#-----------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
#-------------------reduce-------------------
numbers = [1, 2, 3, 4, 5]
total = 0
for x in numbers:
    total = total + x
print(total)
#-----------------------------------------
from functools import reduce
def add(a, b):
    return a + b
numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)
#-----------------------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)





print("-------------------------------------------------------------------------------------------------------------")


from functools import reduce
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

def add(x, y):
    return x + y

numbers = [1,2, 3, 4, 5]
# Double each number -> keep only evens -> multiply them
result = reduce(add,
                filter(is_even,
                       map(double, numbers)))
print(result)

# Right pane (lines 75–87)
print("--------------------------------------------------------lambda----------------------------------------------------")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# No function name, no def, no return
# x is auto-assigned for map
# a, b auto-assigned for reduce
result = reduce(lambda a, b: a + b,
                map(lambda x: x ** 2,
                    filter(lambda x: x % 2 == 0, numbers)))
print(result)