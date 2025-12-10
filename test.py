
import math
# def prac():
#     pass
# #     w = int(input("What is the weight of your package?: "))
# #     if w <= 2:
# #         c=10
# #     else: 
# #         c= 10 + 8 * (w-2)
# #     if c > 25:
# #         c=25 
# #     print (f" cost is {c}!")
# #     print("------------------------------")
# #     p = int(input("how many people will be on the bus?: "))
# #     if p % 50 == 0:
# #         bus= p // 50 
# #     else:
# #         bus = (p//50)+1
# #     print(f"you will need {bus} busses! ")
# #     print("------------------------------")
# #     s = int(input("what is your credit score?: "))
# #     if s < 580:
# #         return "poor"
# #     elif s >= 580 and s <= 669:
# #         return "fair"
# #     elif s >= 670 and s <=739:
# #         return "good"
# #     elif s >= 740 and s <= 799:
# #         return "very good"
# #     else:
# #         return "excellent! "
# #     print("------------------------------")
# #     text = input("text")
# #     result=""
# #     for i in text:
# #         if i in "0123456789":
# #             result += "#"
# #         else: 
# #             result += i 
# #     return result
# #     print("------------------------------")
# #     n = int(input("?: "))
# #     total=0
# #     for i in range(1,n+1):
# #         if i % 2 == 0:
# #             total += i**2
# #         else:
# #             total += i**3
# #     return total
# #     print("------------------------------")
# #     age = int(input)
# #     if age < 12:
# #         return "8$"
# #     elif age <=64 and age >=12:
# #         return "12$"
# #     else:
# #         return "10$"
# #     print("------------------------------")
# #     bottles = int(input("b:"))
# #     if bottles % 24 == 0:
# #         result = bottles//24
# #     else:
# #         result = (bottles//24)+1
# #     return result
# #     print("------------------------------")
# #     g=int(input("grade: "))
# #     if g <=100 and g > =90:
# #         return "A"
# #     elif g <=89 and g >=80:
# #         return "B" 
# #     elif g <=79 and g >=70:
# #         return "C"
# #     elif g <= 69 and g >=60:
# #         return "D"
# #     elif g < 60:
# #         return "F"
# #     print("------------------------------")
# #     text = input("text")
# #     result = ""
# #     for i in text:
# #         if i in "AEIOUaeiou":
# #             result += "#"
# #         else:
# #             result += i
# #     return result
# #     print("------------------------------")
# #     n = int(input("yo"))
# #     result=0
# #     for i in range(1,n+1):
# #         result += math.factorial(i)
# #     return result
# #     print("------------------------------")
# #     highscore = [45,90,2,309,234,234453,0]
# #     result = 0 
# #     for i in highscore:
# #         if i > result:
# #             result=i
# #     return result
# #     print("------------------------------")
# #     str= input("text")
# #     result = 0 
# #     for i in str:
# #         if i in "AEIOUaeiou":
# #             result += 1
# #     return result
# #     print("------------------------------")
# #     y= int(input("year: "))
# #     if y % 400 == 0:
# #         return True
# #     elif y % 100 == 0:
# #         return False
# #     elif y % 4 == 0:
# #         return True
# #     else:
# #         return False
# #     print("------------------------------")
# #     t= input("text:")
# #     result=(t[::-1])
# #     return result
# #     print("------------------------------")
# #     list=[0,2,3,5,9,8,24,34,54,80]
# #     result = []
# #     for i in list:
# #         if i%2==0:
# #             result.append(i) 
# #     return result
# #     print("------------------------------")

# def main():
#     # w = int(input("move?: "))
#     # if w <= 1:
#     #     cost=5 
#     # else:
#     #     cost = 5 + 3 * (w-1) 
#     # if cost > 20:
#     #     cost=20 
#     # return cost 
#     # p = int(input('people '))
#     # if p % 12 == 0: 
#     #     v = p//12 
#     # else:
#     #     v = (p//12) + 1 
#     # t = input("test")
#     # o = ""
#     # for i in t:
#     #     if i in "qwertyuioplkjhgfdsazxcvbnm":
#     #         o += "#"
#     #     else: 
#     #         o += i
#     # return o 
#     # z = int(input("num"))
#     # total = 0 
#     # for i in range (1, z+1):
#     #     if z % 2 == 0:
#     #         total += i**2 
#     #     else: 
#     #         total += i**3
#     # return total
#     # r = int(input("parking"))
#     # if r < 2: 
#     #     cost = 5 
#     # else:
#     #     cost = 5 + 2*(r-2)
#     # if cost > 15:
#     #     cost = 15 
#     # return cost
#     # p = int(input("pizza"))
#     # s = int(input("[peie]"))
#     # if (p*s)% 8 == 0: 
#     #     pizza = (p*s)//8
#     # else:
#     #    pizza = (p*s)//8 +1
#     # return pizza
#     # temp = int(input("temp"))
#     # if temp < 32:
#     #     return "frezzing"
#     # elif temp <= 59 and temp >=32:
#     #     return "cold"
#     # elif temp <= 85 and temp >= 60: 
#     #     return "warm"
#     # else:
#     #     return "hot"
#     # text = input("r")
#     # result= ""
#     # for i in text:
#     #     if i in "bcdfghjklmnpqrstvwxyz":
#     #         result += "#"
#     #     else: 
#     #         result += i 
#     # return result
#     # z = int(input("loop"))
#     # result = 0 
#     # for i in range (1, z+1):
#     #         result += i**2
#     # return result
#     h = int(input("hours?: "))
#     if h <= 4:
#         cost = 5 * h 
#     elif h > 4 and h <=10:
#         cost = 5 + 1.5 *(h-4)
#     if cost > 10:
#         cost = 15
#     return cost 


# if __name__=="__main__":
#    print(main())

# print("-----------------------------------")

def evenSumCount(numbers):
    x =[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i]+numbers[j]) % 2 == 0:
                x += [numbers[i],numbers[j]]
            else:
                pass
    return x

#     count = 0 
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if (numbers[i] + numbers[j]) % 2 == 0:
#                 count += 1 
#             else:
#                 pass
#     return count
# print("-----------------------------------")




def doubleNeighbors(s):
    pass
    # s = s.lower()
    # results = s[0]
    # for i in range(1, len(s)-1):
    #     results += s[i]
    #     if s[i-1] == s[i] == s[i+1]:
    #         results += s[i]
    # results += s[-1]
    # return results



    # results = ""
    # for ch in range(len(s)):
    #     results += s[ch]
    #     if ch < len(s) - 2 and s[ch] == s[ch+1] == s[ch+2]:
    #         results += s[ch] * 3
    # return results
  
    #     s = s.lower()
    #     results = " "
    #     for ch in range (len(s)):
    #         results += s[ch]
    #         if  ch < len(s) - 1 and s[ch] == s[ch + 1]:
    #             results += s[ch]
    #     return results
    
def calculateTotal(smart, premium, isMember):
    pass











    # BasePlan = 10 
    # Music = 3 
    # Video = 5 
    # Tax = 1.06
    # SubTotal = BasePlan + (Musicaddon * Music) + (Video * Videoaddon)
    # if Musicaddon >= 4:
    #     discount = (Musicaddon //4) * 3
    #     SubTotal -= discount
    # if Musicaddon > 0 and Videoaddon > 0:
    #     SubTotal -= 2
    # Final = SubTotal * Tax
    # return Final
        





# def frequentWords(s):
#     punctuation = ["'.' , ',' , '?' , '!' "]
#     s = s.lower()
#     X = ""
#     for ch in s:
#         if ch not in punctuation:
#             X += ch
#     words = X.split()
#     freq = {}
#     for word in words:
#         if word in freq:
#             freq[word] += 1 
#         else:
#             freq[word] = 1
#     return freq

 
def main():
    print(evenSumCount([1,2,3,4,3,2,1])) 
    print(evenSumCount([2,2,2]))
    print(evenSumCount([1,3,5]))
    print(evenSumCount([1,2]))
    # # print(evenSumCount([7,1,5]))    
    print("--------------------------")
    # print(doubleNeighbors("boo"))    
    # print(doubleNeighbors("bookkeeper"))
    # print(doubleNeighbors("aaaah")) 
    # print(doubleNeighbors("abc")) 
    # print("--------------------------")
    # print(calculateTotal(6,2,True))
    # print("--------------------------")
    # print(frequentWords("The cat and the dog."))
    # print(frequentWords("Wow! Wow! What a day, what a great day."))
    # print("--------------------------")



if __name__ == "__main__":
    main()



