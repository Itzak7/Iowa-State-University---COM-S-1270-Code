#Isaac Aguilar                       9-22-25 
#Lab week 4, This is a code that takes 3 different inputs and calculates the product betwwn b and c 

import random 

def randomProduct(a,b,c):
    product= 1
    for i in range (a): 
        num=random.randrange(b,c+1)
        product=product*num  
    return product

def main(): 
    a=int(input("Enter a value for a (how many times you will multiply): "))
    b=int(input("Enter a value for B (your starting range): "))
    c=int(input("Enter a value for c (your ending range): "))
    answer=randomProduct(a,b,c)
    print("The answer is,", answer)

if __name__=="__main__":
    main()