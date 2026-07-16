colors = ["red", "green","blue"]
colors.append("vintage")
colors.insert(3, "pink")
colors.sort()
print(colors)
print(len(colors))


numbers =  [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
numbers.sort()
numbers.reverse()
print(numbers)
print(len(numbers))


point = ("x=10", "y=20", "z=30")
x, y, z = point

print(x)
print(y)
print(z)

navy_blue = (5, 0, 128)
red, green, blue = navy_blue
print(f"the RGB color palette value of NAVY-BLUE is \n > red = {red}\n > green = {green} \n > blue = {blue}")

grades = [88, 72, 95, 60]
grades.sort()
print(sorted(grades))
print(grades)
