
import random


def numbers():
    Y = []
    X = random.randint(200,501)
    for i in range(X):
        Z = random.randint(1,2001)
        Y.append(Z)
    return Y

def findMean(Y):
    W = 0 
    for i in Y:
        W = W + i 
    Mean = W / len(Y)
    return (f"Your Mean is: {Mean}!")

def findMedian(Num):
   Num.sort()
   V = len(Num)
   if V % 2 == 0:
       L = Num[V//2 - 1]
       I = Num [V//2]
       K = (L+I)/2
       return (f"Your Median is: {K}!")
   else:
       Middle = V//2 
       return (f"Your Median is: {Num[Middle]}!")
       

def main():
    Num = numbers()
    Mean = findMean(Num)
    print(Mean)
    Median = findMedian(Num)
    print(Median)


if __name__ == "__main__":
    main()