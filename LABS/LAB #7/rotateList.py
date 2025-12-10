def getNumbers():
    numbers = []
    while True:
        num = input("Please enter a number of your choice! (please input * to stop): ")
        if num == "*":
            break 
        else:
            numbers.append(num)
    return numbers

def rotatedList(Num,rotation):
    X = len(Num)
    if rotation < 0:
        rotations = (-rotation) % X
        return Num[rotations:] + Num[:rotations]
    else:
        rotations = rotation % X
        return Num[-rotations:] + Num[:-rotations]


def main():
    Num = getNumbers()
    rotation = int(input("How many units would you like to slide your list over?: "))
    NewList = rotatedList(Num,rotation)
    print(f"Your list based of {rotation} rotations:{NewList}")


if __name__=="__main__":
    main()