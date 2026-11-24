s="""This is not a 
        string"""


name = "\nMy name is \"Athul\""
print(s,name)


age=23
print("My age is:"+str(age))



ss="Hi"
res=bool(ss)
print(res)



s1="python"
s2="python"
print(s1,id(s1))
print(s2,id(s2))
print(s1 is s2)
print(s1 == s2)


s1="hello"
print(s1)
print(s1,id(s1))
s1=s1+"world"
print(s1,id(s1))


s="athul"
print(s.upper())
