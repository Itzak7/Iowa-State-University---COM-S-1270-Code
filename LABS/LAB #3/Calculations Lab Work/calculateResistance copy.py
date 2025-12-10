#Isaac Aguilar         9-16-2025
#Lab week 2 resistance=voltage/current

#citation- URL: https://study.com/learn/lesson/resistance-equation-derivation.html#section---HowToCalculateVoltageThroughAResistor
#citation- Authour: Coralie Nettles, Yuanxin (Amy)Yang Alcocer, Christianlly Cena
#citation- Date published: Last updated 11/21/2023
#citation- Date accessed: 9/16/2025 
#definition- "r=v/i The R stands for resistance, the V stands for voltage, and the I stands for current. Your units are ohms for resistance, volts for voltage, and amps for current. This formula tells you that your resistance is always equal to your voltage divided by the current." 
# v=int(input("Please enter a value for 'v':")) 
# i=int(input("Please enter a value for 'i':"))
# r=v/i 
# print(f"The result of {v}/{i}={r}") 

def Resistancecalculation(Voltage,Current): 
    return Voltage/Current  

def main(): 
    v=int(input("Please enter a value for voltage:")) 
    i=int(input("Please enter a value for current:")) 
    r=Resistancecalculation(v,i) 
    print(f"The result of {v}/{i}={r}")  

if __name__== "__main__": 
    main()