trainers = ["Divya", "Gamana", "Salman", "Gamana", "Salman", "Gamana"] 
trainer_count = {}

for t in trainers:
    if t in trainer_count:
        trainer_count[t] += 1
    else:
        trainer_count[t] = 1

print(trainer_count)


from collections import Counter

trainers = ["Divya", "Gamana", "Salman", "Gamana", "Salman", "Gamana"]
trainer_count = Counter(trainers)

print(trainer_count)




stu_info = {
    "asha": {"cs": 48, "py": 78},
    "ravi": {"cs": 48, "py": 78}
}

# Accessing & updating (Note: whiteboard wrote stu_info["marks"]["py"], corrected here to match the keys)
print(stu_info["ravi"]["py"])   # Output: 78
stu_info["ravi"]["py"] = 90
print(stu_info["ravi"]["py"])   # Output: 90
# Traversing
for k, v in stu_info.items():
    print(k)
    for sub, mark in v.items():
        print(sub, mark)