#Isaac Aguilar.                     9-22-2025 
#Lab week 4, This code approximates the square root using iterations 

def sqrtIter(x,iterations):
    y=(x+1)/2 

    for i in range(iterations):
        y_n=((x/y)+y)/2  
        y=y_n
    return y 


def main():
    X=int(input("Please enter a value to find the square root of:"))
    I=int(input("Please enter a value for interations:")) 
    answer=sqrtIter(X,I)
    print("Your square root estimation of,",X, "after,", I,"iterations is:",answer) 

if __name__=="__main__":
    main() 
