

def findSubStringV1(M,S):
    X = M.find(S)
    if X != -1:
        print(f"Your substring was found at position {X}!")
    else: 
        print(f"Your substring was at {X}, which means it was NOT found!")

def findSubStringV2(M,S):
    if S in M:
         X = M.index(S)
         print(f"Your substring was found at position {X}!")
    else:
        print("Your substring was NOT found! ")

def findSubStringV3(M,S):
    for x in range(len(M)-len(S)+1):
        for o in range(len(S)):
            if M [x + o] != S[o]:
                break
        else:
            print((f"Your substring was found at position {x}!"))
            return
    print("Your substring was NOT found! ")
                




def main():
    M = input("Please enter your main string! : ") 
    S = input("please enter the substring you wish to search for! : ") 
    findSubStringV1(M,S)
    findSubStringV2(M,S)
    findSubStringV3(M,S)


if __name__=="__main__":
    main()