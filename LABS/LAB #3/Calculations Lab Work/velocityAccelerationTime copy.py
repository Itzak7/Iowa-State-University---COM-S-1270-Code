#Isaac Aguilar         9-16-2025
#Lab week 2 velocity+(acceleration*time)

#citation- URL: https://study.com/skill/learn/using-kinematic-equations-to-solve-for-an-unknown-final-velocity-explanation.html
#citation- Authour: Margaret Bruff, Kirsten Wordeman
#citation- Date published: Not available 
#citation- Date accessed: 9/16/2025 
#definition- "V(f)=V(i)+at where V(i) is the initial velocity, V(f) is the final velocity, a is the acceleration, and t is the time duration"
# a=int(input("Please enter a value for 'a':")) 
# t=int(input("Please enter a value for 't':"))
# Vi=int(input("Please enter a value for 'Vi':")) 
# Vf=Vi+(a*t) 
# print(f"The result of ({a}*{t})+{Vi}={Vf}") 

def VelocityCalculation(acceleration,duration,initialvelocity):
    return initialvelocity+(acceleration*duration)

def main():
    a=int(input("Please enter a value for acceleration:")) 
    t=int(input("Please enter a value for duration:"))
    Vi=int(input("Please enter a value for initial velocity:")) 
    Vf=VelocityCalculation(a,t,Vi)
    print(f"The result of ({a}*{t})+{Vi}={Vf}")  

if __name__=="__main__":
    main()