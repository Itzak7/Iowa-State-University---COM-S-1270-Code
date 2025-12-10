#Isaac Aguilar         9-16-2025
#Lab week 2 apr=((((interest+fees)/loan)/days)*365)*100

#citation- URL: https://www.capitalone.com/learn-grow/money-management/how-to-calculate-apr-on-credit-card/
#citation- Authour: Capital One
#citation- Date published: 1/9/2025
#citation- Date accessed: 9/16/2025 
#definition- " APR represents the annual cost of borrowing money, shown as a percentage. The formula to calculate APR is: APR = (((Interest + Fees ÷ Loan amount) ÷ Number of days in loan term) x 365) x 100."
# i=int(input("Please enter a value for 'i':"))
# f=int(input("Please enter a value for 'f':"))
# l=int(input("Please enter a value for 'l':"))
# d=int(input("Please enter a value for 'd':")) 
# apr=((((i+f)/l)/d))*100
# print(f"The result of (((({i}+{f})/{l})/{d}))*100={apr}") 

def annualpercentagerate(interest,fees,loan,days):
    return ((((interest+fees)/loan)/days))*100 

def main(): 
    i=int(input("Please enter a value for your interest:"))
    f=int(input("Please enter a value for your fees:"))
    l=int(input("Please enter a value for your loan :"))
    d=int(input("Please enter a value for your days:")) 
    apr=annualpercentagerate(i,f,l,d)
    print(f"The result of (((({i}+{f})/{l})/{d}))*100={apr}")  

if __name__=="__main__":
    main()