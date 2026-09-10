# Cesar Cano
# Python Program #2

def rect_area(rect_base, rect_height):
    area = rect_base * rect_height
    return area

base = int(input("Enter the base of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

result = rect_area(base, height)

print("The area of the rectangle is", result)
