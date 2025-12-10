
def CompoundAmount(principle,interstrate,amountofinterest,numberofyears): 
    return  principle*(1+(interstrate/100)/amountofinterest)**(amountofinterest*numberofyears) 

def annualpercentagerate(interest,fees,loan,days):
    return ((((interest+fees)/loan)/days))*100 