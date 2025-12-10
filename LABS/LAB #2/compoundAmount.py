#Isaac Aguilar         9-16-2025
#Lab week 2 accured amount=priciple*(1+(rate/100)compound)^(compounds*time)

#citation- URL: https://study.com/academy/lesson/compounding-interest-formulas-calculations-examples.html
#citation- Authour: Ryan Johnson, Jeff Calareso, Amy Fredrickson
#citation- Date published: Last updated 11/21/2023
#citation- Date accessed: 9/16/2025 
#definition- "Compound interest can be calculated using the compound interest formula: I = P((1+(r/n))^(nt) Where I = Interest P = Principle, the original amount r = interest rate, as a decimal n = number of times the interest is compounded in a year t = number of years" 
p=int(input("Please enter a value for 'p':"))
r=int(input("Please enter a value for 'r':"))
n=int(input("Please enter a value for 'n':"))
t=int(input("Please enter a value for't':")) 
i=p*(1+(r/100)/n)**(n*t) 
print(f"The result of {p}(1+({r}/100)/{n})^{n*t}={i}") 

