from utilities import circle_area, rectangle_area, triangle_area

area = 0
shape_choice = input("Enter a shape to find its area: \nCircle \nRectangle \nTriangle")

if shape_choice.lower() == 'circle':
    radius = input("Please enter the radius of the needed circle")
    area = circle_area(radius=radius)

elif shape_choice.lower() == 'rectangle':
    length = input("Please enter the lenght of the needed rectangle")
    width = input("Please enter the width of the needed rectangle")
    area = rectangle_area(length=length, width=width)

elif shape_choice.lower() == 'triangle':
    height = input("Please enter the height of the needed triangle")
    base = input("Please enter the base of the needed triangle")
    area = circle_area(base=base, height=height)

else:
    print(f"Selected shape is not supported {shape_choice.lower()} - Please choose an item from the list")

print(f"Calculated area for {shape_choice} is {area}")
