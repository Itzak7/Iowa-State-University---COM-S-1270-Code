#Isaac Aguilar         9-16-2025
#Lab week 2 circumference of a circle 

#citation- URL: https://study.com/learn/lesson/circumference-cirlce-formula-area.html#section---AreaAndCircumferenceOfACircle
#citation- Authour: Danielle Sands, Damien Howard
#citation- Date published: Last updated 11/21/2023
#citation- Date accessed: 9/16/2025 
#definition-"The circumference can by found by using the formula: 2(Pi)r. This works by multiplying Pi (3.14) by the radius and then by 2."

# import math 
# r=int(input("Please enter a value for 'r':"))
# pi=math.pi
# c=2*pi*r
# print(f"The result of 2*{pi}*{r}={c}") 

import math 
def CircleCircumference(radius):
    return 2*math.pi*radius   

def main(): 
    r=int(input("Please enter the radius of the circle:"))
    pi=math.pi
    c=CircleCircumference(r)
    print(f"The result of 2*{pi}*{r}={c}") 

if __name__=="__main__": 
    main()