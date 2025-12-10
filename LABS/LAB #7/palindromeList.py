def gettingTheGoods():
    Words= []
    while True:
        McChicken = input("Please enter a word of your choice! (Input '*' when you wish to stop): ")
        if McChicken == "*":
            break 
        else: 
            Words.append(McChicken )
    return Words

def checkingIfPalindrome(Words):
    for i in range (len(Words)//2):
       if  Words[i] != Words[-(i+1)]:
           return ("Your list of words IS NOT palindrome!")      
    return ("Your list of words IS A palindrome!")
        
def main():
   listOfWords = gettingTheGoods()
   print(listOfWords)
   Result = checkingIfPalindrome(listOfWords)
   print(Result)
  

if __name__ == "__main__":
    main()