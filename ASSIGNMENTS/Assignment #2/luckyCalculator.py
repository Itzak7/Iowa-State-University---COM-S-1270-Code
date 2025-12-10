#Isaac Aguilar                    9-23-2025 
#Assessment #2                  Lucky Calculator  
#
#This assesment is a lucky calculator that can do 7 different operations with any integer and produces a product 
# from the user inputs.This lucky calulator can also produce a lucky number, and has a quit option if the user does'nt want to any of that.

import random

print("Lucky Calculator!") 
print() 
print("By:Isaac Aguilar") 
print("[COMS 1270  4]") 
print()
print("What would you like to do today?") 
choice=input("[C]alculator, [L]ucky Number, [Q]uit:").upper() 

if choice=="C":
    print()
    print("You chose Calculator, YAY!")
    print() 
    op=input("Please chose your operation for today! [+], [-], [*], [/], [//], [%], [**]:") 
    if op=="+":
        X=int(input("Please enter your first value for your addition calculation!" )) 
        Y=int(input("Please enter your second value for your addition calculation!"))
        Answer=X+Y
        print(f"Your answer from the calculation {X}+{Y}={Answer}") 
    elif op=="-":
        X=int(input("Please enter your first value for your subtraction calculation!:"))  
        Y=int(input("Please enter your second value for your subtraction calculation!:"))
        Answer=X-Y 
        print(f"Your answer for your calculation {X}-{Y}={Answer}") 
    elif op=="*": 
        X=int(input("Please enter your first value for your multiplication calculation!:"))  
        Y=int(input("Please enter your second value for your multiplication calculation!:"))
        Answer=X*Y 
        print(f"Your answer for your calculation {X}*{Y}={Answer}") 
    elif op=="/": 
        X=int(input("Please enter your first value for your division calculation!:"))  
        Y=int(input("Please enter your second value for your division calculation!:")) 
        if Y==0: 
         print("UH OH! Sorry you cannot divide by 0! Please try again with another value!")
        else: 
            Answer=X/Y
            print(f"Your answer for your calculation {X}/{Y}={Answer}")  
    elif op=="//": 
        X=int(input("Please enter your first value for your floor division calculation (division with rounding)!:"))  
        Y=int(input("Please enter your second value for your floor division calculation (division with rounding)!:")) 
        if Y==0: 
            print("UH OH! Sorry you cannot floor divide by 0! Please try again with another value!")
        else: 
            Answer=X//Y
            print(f"Your answer for your calculation {X}//{Y}={Answer}")  
    elif op=="%": 
        X=int(input("Please enter your first value for your modulus calculation (division but gives the remainder)!:"))  
        Y=int(input("Please enter your second value for your modulus calculation (division but gives the remainder)!:")) 
        if Y==0: 
            print("UH OH! Sorry you cannot do a modulus calculation by 0! Please try again with another value!")
        else: 
            Answer=X%Y
            print(f"Your answer for your calculation {X}%{Y}={Answer}")    
    elif op=="**": 
        X=int(input("Please enter your base value for your exponent calculation!:"))  
        Y=int(input("Please enter your raised value for your exponent calculation!:"))  
        Answer=X**Y
        print(f"Your answer for your calculation {X}**{Y}={Answer}")  

elif choice=="L":
    print("You chose Lucky Number, YAY!")  
    print()
    A=int(input("Please enter a value to calculate your lucky number!:"))
    B=int(input("Please enter a second value to calculate your lucky number!:"))
    luckynumber=random.randrange(A,B+1) 
    print(f"Your Lucky Number is {luckynumber}, hope you like it! no refunds!")
    print()

elif choice=="Q":
    print("You chose to quit! bye bye, hope to see you soon!")
else:
    print("OOOPS! You did not choose a vaild choice. Please try again!")


    