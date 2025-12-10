
def multiplicationTable(Ln,Hn):
    for I in range (Ln,Hn+1):  
        for R in range (Ln,Hn+1): 
            print(repr(I*R).rjust(3), end=" ")
        print()


def main():
    Ln=int(input("what would you like your low number of your multiplication table to be?: "))
    Hn=int(input("what would you like your high number of your multiplication table to be?: "))
    multiplicationTable(Ln,Hn)



if __name__=="__main__":
    main()