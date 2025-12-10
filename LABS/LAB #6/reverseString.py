
def reverseStringV1(R):
    return R[::-1]

def reverseStringV2(R):
    Word=R
    WordR="".join(reversed(Word))
    return WordR

def reverseStringV3(R):
    wordRev = ""                                      
    for i in range(len(R)-1,-1,-1,):                    
        wordRev += R[i]
    return wordRev

def reverseStringV4(R):
    wordRev = ""
    for i in R:
        wordRev = i + wordRev
    return wordRev

def reverseStringV5(R):
    wordRev = ""
    i = len(R)-1
    while i >=0 :
        wordRev += R[i]
        i -= 1
    return wordRev


def main():
    R=str(input("What word would you like reversed?: "))
    print (reverseStringV1(R))
    print (reverseStringV2(R))
    print (reverseStringV3(R))
    print (reverseStringV4(R))
    print (reverseStringV5(R))


if __name__=="__main__":
    main()