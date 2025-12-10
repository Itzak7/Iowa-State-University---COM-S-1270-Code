#Isaac.     10-1-2025 
#finding leap year 


def leapyear(year,):
    if year % 400 == 0:
        return "YES"
    elif year % 100 == 0: 
        return "NO" 
    elif year % 4 == 0:
        return "YES" 


def main():
    year=int(input("please enter the year you would like to test to see if it's a leap year!: "))
    answer=leapyear(year)
    if answer=="YES": 
        print(f"{answer}!, your year '{year}', is a leap year!")
    elif answer=="NO": 
        print(f"{answer}!, your year '{year}', is not leap year!")



if __name__=="__main__":
    main()