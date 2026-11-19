#Dictionaries - {key:Value} - key value pair , key should be unique, ordered 
#key is immutable and value can be everything
#Values can be anything - dupliicates allowed 

from Tuple import stu_info
dict1= {"name":"John", "age":30, "city": ["New York", "USA", "Germany"]}
dict1["name"]="Doe"
print(dict1,dict1.values(),dict1.keys(),dict1.items())
print(type(dict1), dict1["name"],dict1["city"][1])

#Constructor
stu_info=dict(name="Ram",age=20,city="USA")
print(stu_info)
stu_info["salary"]=50000
print(stu_info)
stu_info.update({"salary":20000})
print(stu_info)
stu_info.pop("age")
print(stu_info)
stu_info.popitem()
print(stu_info)
del stu_info["city"]
print(stu_info)
stu_info.clear()
print(stu_info)
del stu_info
#print(stu_info)

#loop dicts
dict1= {"name":"John", "age":30, "city": ["New York", "USA", "Germany"]}
for i in dict1.values():
    print(i)

for i in dict1.keys():
    print(i)

for i in dict1.items():
    print(i)

#Dict Methods
print(dict1.get("name"))
print(dict1.get("salary",0))

#fromkeys
print(dict1.fromkeys(["name","age"]))

#setdefault
print(dict1.setdefault("name","John"))

#copy
dict2=dict1.copy()
print(dict2)