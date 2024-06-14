# Python Program to find Diameter, Circumference, and Area Of a Circle


def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * 3.14 * radius

def find_Area(radius):
    return 3.14* radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("Diameter Of a Circle ",diameter)
print("Circumference Of a Circle",circumference)
print("Area Of a Circle ",area)