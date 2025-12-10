
def studentLoanAmortization(P,I,Y):
    numberOfPayments = Y * 12 
    monthlyInterestRate= I / 12
    monthlyPayment= P * ((monthlyInterestRate * (1 + monthlyInterestRate)**numberOfPayments)) / ((1 + monthlyInterestRate)**numberOfPayments -1)
    Balance= P
    print()
    print("Period".ljust(9),"Total Payment Due".ljust(20), "Computed Interest".ljust(20), "Principal Due".ljust(20), "Principal Balance")
    for Z in range (1,numberOfPayments+1):
        interestOfMonth = Balance * monthlyInterestRate
        principalPortion = monthlyPayment - interestOfMonth 
        Balance = Balance - principalPortion   
        print(repr(round(Z,2)).ljust(9), repr(round(monthlyPayment,2)).ljust(20), repr(round(interestOfMonth,2)).ljust(20), repr(round(principalPortion,2)).ljust(20), repr(round(Balance,2)))
    


def main():
    P=float(input("Please input your principal to calculate your amortization: "))
    I=float(input("Please input your yearly interest to calculate your amortization: "))
    Y=int(input("Please input your number of years to calculate your amortization: "))
    studentLoanAmortization(P,I,Y)



if __name__=="__main__":
    main()