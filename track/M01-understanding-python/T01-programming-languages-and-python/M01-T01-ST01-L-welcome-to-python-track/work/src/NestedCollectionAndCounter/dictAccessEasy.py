products = [
    {"code": "P101", "name": "Keyboard", "price": 1200},
    {"code": "P102", "name": "Mouse", "price": 600},
    {"code": "P103", "name": "Monitor", "price": 8500}
]

product_by_code = {}

for product in products:
    code = product["code"]

    if code not in product_by_code:
        product_by_code[code] = product

required_code = input("Enter the product code: ")

product = product_by_code.get(required_code)

if product is None:
    print("Product not found")
else:
    print("Name:", product["name"])
    print("Price:", product["price"])


#Collection of dictionary with same keys for grouping


students = [
    {"name": "Asha", "course": "Python"},
    {"name": "Ravi", "course": "Java"},
    {"name": "Meera", "course": "Python"},
    {"name": "Kiran", "course": "SQL"}
]

students_by_course = {}

for student in students:
    course = student["course"]
    name = student["name"]

    if course not in students_by_course:
        students_by_course[course] = []

    students_by_course[course].append(name)
print(students_by_course)



