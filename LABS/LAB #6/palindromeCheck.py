

import reverseString
def palindromeCheckV1(R):
    U = reverseString.reverseStringV2(R)
    if R == U: 
        print ("Your word is a palindrome! ")
    else: 
        print("Your word is not a palindrome! ")

def palindromeCheckV2(R):
    for i in range (len(R) // 2):
        if R[i] != R[len(R)-1-i]:
            print("Your word is not a palindrome! ")
            return   
        else:
            print ("Your word is a palindrome! ")
        



def main():
    R=str(input("What word would you like to check to see if it is a palindrome?: "))
    palindromeCheckV1(R)
    palindromeCheckV2(R)




if __name__=="__main__":
    main()