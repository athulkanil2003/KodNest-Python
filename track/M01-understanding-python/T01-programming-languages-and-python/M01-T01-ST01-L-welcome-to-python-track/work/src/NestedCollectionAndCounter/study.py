students = [
{"name": "Asha", "course": "Python"},
{"name": "Ravi" ,"course": "Java"},
{"name": "Meera", "course": "Python"},
{"name": "Kiran", "course": "SQL"}
]

student_by_course={}

for student in students:
    c=student["course"]
    n=student["name"]

    if c not in student_by_course:
        student_by_course[c]=[]
    
    student_by_course[c].append(n)

print(student_by_course)




#Groupby course in  python




def group_students(students):
    students_by_course = {}

    for name, course in students:
        students_by_course.setdefault(course, []).append(name)

    return students_by_course

# Sample data embedded directly in the code
students = [
    ("Asha", "Python"),
    ("Ravi", "Java"),
    ("Meera", "Python"),
    ("Kiran", "SQL"),
    ("Nisha", "Java")
]

students_by_course = group_students(students)

for course, names in students_by_course.items():
    print(course + ": " + " ".join(names))