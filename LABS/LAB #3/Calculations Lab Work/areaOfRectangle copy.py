#Isaac Aguilar.                9-16-2025 
#Lab week 2- area of rectangle 

#citation- URL: https://study.com/skill/learn/how-to-calculate-the-area-of-a-rectangle-explanation.html
#citation- Authour: Kayla Zeliff, Amy Mayers
#citation- Date written: Not available
#citation- Date Accessed: 9-16-2025

#definition- "Area of a Rectangle: A rectangle's area can be obtained by using the equation A= L*W where L is the length and W is the width. The length is usually seen as the longer side unless specified by the problem."

#a=int(input("Please enter a value for 'a':"))
#b=int(input("Please enter a value for 'b':"))
#c= a + b 
#print(f"the result of {a}+{b}={c}")

def areaOfRectangle (width, height ): 
    return width*height


def main():
    a=int(input("Please enter a value for width:"))
    b=int(input("Please enter a value for height:"))
    c=areaOfRectangle(a,b) 
    print(f"the result of {a}*{b}={c}") 

if __name__ == "__main__":
    main()
   

