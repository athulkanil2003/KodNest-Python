c=50
def add():
    global a
    a=10
    global b
    b=30
    print(c)
    #c=30
    print("a+b==>",a+b)
    print("c==>",c)

add()
print("a+b==>",a+b)
print("c==>",c)