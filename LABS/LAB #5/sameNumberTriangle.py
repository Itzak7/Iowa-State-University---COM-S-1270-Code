

def sameNumberTriangle(N):
    for i in range(0,N+1): 
        for n in range (1, i+1):
            print(i, end= " ")
        print()


def main():
    N=int(input("How many number lines would you like?: "))
    sameNumberTriangle(N)


if __name__=="__main__":
    main()