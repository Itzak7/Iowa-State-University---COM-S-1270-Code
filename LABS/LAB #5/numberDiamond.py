
def numberDiamond(N):
    for I in range (0,N+1):
            print (" "* (N-I), end=" ")
            for U in range (1,I+1):    
                print (U, end=" ")
            print()
    
    for L in range (N-1,0,-1):
            print (" "* (N-L), end=" ")
            for M in range (1,1+L):
                 print(M, end=" ")
            print()


def main():
    N=int(input("How many lines would you like in your number diamond?: "))
    numberDiamond(N)


if __name__=="__main__":
    main()

