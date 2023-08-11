import math 


def CircleArea(radius):
    
    area = radius**2 * math.pi
    
    return area

Radius = float(input("please enter the radius of the given circle: "))

print("The area of the given circle is: ", CircleArea(Radius))