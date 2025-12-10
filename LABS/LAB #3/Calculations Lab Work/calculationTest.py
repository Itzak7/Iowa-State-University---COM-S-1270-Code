#Isaac Aguilar             9-25-2025 
#
#yep 

import math
import myShapes
import myFinances 
import myOhmsLaw 
import myPhysics

def main():
    while True:
        choices=input("Hello! What would you like to calculate today? [S]hapes,[F]inances,[O]hms Law,[P]hysics,or would you like to [Q]uit?: ").upper()
        
        if choices== "S": 
            print()
            formula=input("What formula for a shape would you like to work with? [A]rea of Rectangle,[C]ircle Circumference,[R]ectangle Perimeter,or [AC]rea of Circle?: ").upper()
        
            if formula=="A":
             a=int(input("Please enter a value for width:"))
             b=int(input("Please enter a value for height:"))
             answer=myShapes.areaOfRectangle(a,b) 
             print(f"the result of {a}*{b}={answer}")  
            
            elif formula=="C":
                r=int(input("Please enter the radius of the circle:")) 
                pi=math.pi
                answer=myShapes.CircleCircumference(r)  
                print(f"The result of 2*{pi}*{r}={answer}")  
            
            elif formula=="R":
             l=int(input("Please enter a value for length"))
             w=int(input("Please enter a value for width"))
             answer=myShapes.RectanglePerimeter(l,w)
             print(f"the result of ({l}+{w})*2={answer}")  

            elif formula=="AC":
               r=int(input("Please enter a value for radius:")) 
               answer=myShapes.areaOfCircle(r)
               print(f"the result of {math.pi}*({r}**2)={answer}")  

            else:
              print("OOOPS! you entered something out of my knowledge. Please try again!")
        
        elif choices=="F":
           print()
           formula2=input("What finance forumula would you like to work with? [C]ompound Amount or [A]nnual percentage rate?: ").upper()
           
           if formula2=="C":
             p=int(input("Please enter a value for principle:"))
             r=int(input("Please enter a value for the interst rate:"))
             n=int(input("Please enter a value for the amount of times the interst is compunded in the year:"))
             t=int(input("Please enter a value for the number of years:")) 
             answer=myFinances.CompoundAmount(p,r,n,t)
             print(f"The result of {p}(1+({r}/100)/{n})^{n*t}={answer}") 
            
           elif formula2=="A": 
            i=int(input("Please enter a value for your interest:"))
            f=int(input("Please enter a value for your fees:"))
            l=int(input("Please enter a value for your loan :"))
            d=int(input("Please enter a value for your days:")) 
            answer=myFinances.annualpercentagerate(i,f,l,d)
            print(f"The result of (((({i}+{f})/{l})/{d}))*100={answer}")  

           else:
              print("OOOPS! you entered something out of my knowledge. Please try again!")
        
        elif choices=="O":
           print()
           formula3=input("Which Ohams Law would you like to work with? [C]urrent,[R]esistance,or [V]oltage?: ").upper()
           
           if formula3=="C":
             v=int(input("please enter a value for voltage:")) 
             r=int(input("Please enter a value for resistance:"))  
             answer=myOhmsLaw.CurrentCalculation(v,r)
             print(f"The result of {v}/{r}={answer}") 
           
           if formula3=="R":
             v=int(input("Please enter a value for voltage:")) 
             i=int(input("Please enter a value for current:")) 
             answer=myOhmsLaw.Resistancecalculation(v,i) 
             print(f"The result of {v}/{i}={answer}")  
           
           if formula3=="V":
             i=int(input("Please enter a value for currnet:")) 
             r=int(input("Please enter a vaule for resisitance:"))
             answer=myOhmsLaw.CalculateVolatage(i,r)
             print(f"The result of {i}*{r}={answer}") 

           else:
              print("OOOPS! you entered something out of my knowledge. Please try again!")
        
        elif choices=="P":
           print()
           formula4=input("Which Physics formula would you like to work with? [V]elocity or [D]istance?").upper()

           if formula4=="V":
              a=int(input("Please enter a value for acceleration:")) 
              t=int(input("Please enter a value for duration:"))
              Vi=int(input("Please enter a value for initial velocity:")) 
              answer=myPhysics.VelocityCalculation(a,t,Vi)
              print(f"The result of ({a}*{t})+{Vi}={answer}")   
           
           elif formula4=="D":
             s=int(input("Please enter a value for speed:")) 
             t=int(input("Please enter a value for time:")) 
             answer=myPhysics.DistanceCalculation(s,t)
             print(f"The result of {s}*{t}={answer}")  
           
           else:
              print("OOOPS! you entered something out of my knowledge. Please try again!")

        elif choices== "Q": 
            print("Ok bye bye! come again soon!") 
            break
        
        else:
            print("OOOPS! you entered something out of my knowledge. Please try again!")

if __name__=="__main__":
    main()