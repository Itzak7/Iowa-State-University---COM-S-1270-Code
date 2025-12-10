#Isaac Aguilar                  9-22-2025   
#Lab week 4. Drawing a tridecagon

import turtle 

def tridecagonTurlte(s,x,y,t):

    t.penup()
    t.goto(x,y)
    t.pendown()
    angle=360/13 
    for i in range (13):
     
     t.forward(s)  
     t.right(angle) 
    
def main(): 
    s = int(input("Enter the side length of the tridecagon: "))
    x = int(input("Enter the x coordinate of the first vertex: "))
    y = int(input("Enter the y coordinate of the first vertex: "))
    t=turtle
    tridecagonTurlte(s,x,y,t)
    turtle.done() 

if __name__=="__main__":
   main()
