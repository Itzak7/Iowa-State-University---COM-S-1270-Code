def numbers():
    numbers = []
    while True:
        num = input("Please enter a number of your choice! (please input * to stop): ")
        if num == "*":
            break 
        else:
            numbers.append(num)
    return numbers

def endNum(numbers,Num):
    X = []
    Y = []
    for i in numbers:
        if i == Num: 
            Y.append(i)
        else:
            X.append(i)
    return X + Y


def main():
    abc = numbers()
    print(abc)
    Num = input("What is your special number from your list?: ")
    xyz = endNum(abc,Num)
    print(f"Your new special and really cool list:{xyz}")



if __name__=="__main__":
    main()


