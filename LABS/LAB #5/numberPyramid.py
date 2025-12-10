
def numberPyramid(N):
    for i in range (0,N+1):
        print (" "* (N-i), end=" ")
        for u in range (1,i+1):    
           print (u, end=" ")
        print()
    

def main():
   N=int(input("How many lines would you like in your number pyramid?: "))
   numberPyramid(N)

    

if __name__=="__main__":
    main()