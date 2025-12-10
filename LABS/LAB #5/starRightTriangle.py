
def starRightTriangle(N): 
   for i in range(0,N+1): 
    print ("*"*i)

def main():
   N=int(input("How many star lines would you like?: "))
   starRightTriangle(N)


if __name__=="__main__":
    main()