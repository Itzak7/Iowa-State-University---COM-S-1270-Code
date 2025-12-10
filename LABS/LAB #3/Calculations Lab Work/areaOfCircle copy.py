#Isaac Aguilar         9-16-2025
#Lab week 2 area of circle 

#citation- URL: https://study.com/learn/lesson/circumference-cirlce-formula-area.html#section---AreaAndCircumferenceOfACircle
#citation- Authour: Danielle Sands, Damien Howard
#citation- Date published: Last updated 11/21/2023
#citation- Date accessed: 9/16/2025 
#definition- "The area, A, of a circle can be found by multiplying Pi (3.14) by the radius squared. That is, A = Pi*r^2. Given the circumference, C, of a circle, the area can be found by dividing the circumference by 2, and multiplying that result by the radius. That is, A = (C / 2)r."

# import math 
# r=int(input("Please enter a value for 'r':"))
# pi=math.pi
# a=math.pi*(r**2)
# print(f"the result of {pi}*({r}**2)={a}") 

import math

def areaOfCircle (radius):
    return math.pi*radius**2 
 
def main():
    r=int(input("Please enter a value for radius:")) 
    a=areaOfCircle(r)
    print(f"the result of {math.pi}*({r}**2)={a}")  

if __name__=="__main__":
    main()