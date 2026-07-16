weirdo_1 = {"shapes": "triangle", "sides": 3}
print(weirdo_1["shapes"])
print(weirdo_1.get("fast", "sluggish"))
weirdo_1["shapes"] = "square"
weirdo_1["x_position"] = 0
print(weirdo_1["shapes"])
del weirdo_1["shapes"]
print(weirdo_1["sides"])

fruits = {"apple", "banana", "orange", "almond", "apple"}
print(sorted(fruits))

m = {1, 2, 3}
n = {3, 4, 5}

print(m | n)
print(m & n)
print(m - n)

michael = {"michael.": "python && rust"}
print(michael["michael."])
print(michael.get("car"))

cars = {"bmw", "audi", "mercedes_benz", "koineggseg", "pagani", "audi", "bmw"}
print(sorted(cars))

student = {"name": "Alice", "age": "20", "courses": ["Math", "Physics"]}
print(student["name"])
print(student["age"])
student["gpa"] = 3.9
student["age"] = 21
print(student["age"])
print(student["gpa"])
print(student["name"])
print(student.get("scholarship", "not eligible"))


denim = {1, 2, 3, 4, 4, 5}

denim.add(6)

z = {4, 5, 6, 7}

print(denim)
print(denim | z)








