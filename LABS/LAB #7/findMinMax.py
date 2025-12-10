


def numbers():
    numbers = []
    while True:
        num = input("Please enter a number of your choice! (please input * to stop): ")
        if num == "*":
            break 
        else:
            numbers.append(num)
    return numbers

def minValue(fortnite):
    number = fortnite[0]
    for num in fortnite:
        if num < number:
            number = num 
    return number

def maxValue(fortnite):
    number = fortnite[0]
    for num in fortnite:
        if num > number:
            number = num 
    return number

def main():
    x = [int(x) for x in numbers()]
    print("Your Number List:", x)
    s = minValue(x)
    l = maxValue(x)
    print(f"Your Smallest value from your list was {s}!")
    print(f"Your Largest value from your list was {l}!")



if __name__=="__main__":
    main()