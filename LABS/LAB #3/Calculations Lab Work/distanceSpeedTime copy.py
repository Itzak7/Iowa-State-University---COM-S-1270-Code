#Isaac Aguilar         9-16-2025
#Lab week 2 distance=speed*time

#citation- URL: https://study.com/academy/lesson/distance-formulas-calculations-examples.html#section---DistanceRateTimeFormula
#citation- Authour: Ashley Kelton, Jeff Calareso
#citation- Date published: Last updated 11/21/2023
#citation- Date accessed: 9/16/2025 
#definition-"The standard distance formula, which is also known as the uniform rate formula, is d = rt. D stands for distance, r for rate and t for time."

# s=int(input("Please enter a value for 's':")) 
# t=int(input("Please enter a value for 't':")) 
# d=s*t 
# print(f"The result of {s}*{t}={d}") 

def DistanceCalculation(speed,time):
    return speed*time 
def main(): 
    s=int(input("Please enter a value for speed:")) 
    t=int(input("Please enter a value for time:")) 
    d=DistanceCalculation(s,t)
    print(f"The result of {s}*{t}={d}") 
if __name__=="__main__": 
    main()