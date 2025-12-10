#Isaac Aguilar                  9-30-2025   
#Lab week 5. Drawing multiple tridecagon

import turtle 


def tridecafonTurlte(s,x,y,t):
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle=360/13 
    for i in range (13):
     t.forward(s)  
     t.right(angle)  
    
def drawMultipleTridecagons(sr,nr,y,x,s,t):
  angle=360/13 
  for i in range(1,nr):
        t.penup()
        t.goto(x+(sr*i),y) 
        t.down()
        for i in range (13):
            t.forward(s)  
            t.right(angle)  
     

def main(): 
    s=int(input("Enter the side length of the tridecagon: "))
    x=int(input("Enter the x coordinate of the first vertex: "))
    y=int(input("Enter the y coordinate of the first vertex: "))
    nr=int(input("Enter the number of tridecagon repetitions to be drawn: "))
    sr=int(input("Enter the amount of space between tridecagon repetitions on the x axis:"))   
    t=turtle
    tridecafonTurlte(s,x,y,t,) 
    drawMultipleTridecagons(sr,nr,y,x,s,t)

    turtle.done() 


if __name__=="__main__":
   main()

