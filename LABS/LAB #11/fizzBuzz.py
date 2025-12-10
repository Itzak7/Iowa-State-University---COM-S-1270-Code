# Help from https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
# Date accessed: 12/9/2025

def fizzBuzz(Num):
    Answer = []
    for i in range(1, Num + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if i % 7 == 0:
            s += "Bazz"
        if s == "":
            s = str(i)
        Answer.append(s)
    return Answer

def main():
    number = int(input("Please enter a number!!!: "))
    output = fizzBuzz(number)
    print(output)

if __name__ == "__main__":
    main()
