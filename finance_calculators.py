import math
investment_or_bond = str(input('''Choose either 'investment' or 'bond' from the menu below to proceed
investment-to calculate the amount of interest you'll earn on interest
bond-to calculate the amount you'll have to pay on a home loan
: '''))

#  for investment option the following formula will be used
if investment_or_bond == 'investment':
    amount = float(input("enter the amount you want to deposit"))
    interest_rate = int(input("enter the interest rate,enter the integer only"))
    num_years = int(input("enter the number of years you want to invest"))
    interest = str(input("enter simple or compound interest"))

    if interest == 'simple':         #assigning the formula if thr user has entered simple interest
        simple = (amount * (1 + interest_rate/100 * num_years))
        print(simple)

    elif interest == 'compound':  #assigning the formula if the user has entered compound interest
        compound = ((amount * math.pow((1 + interest_rate/100), num_years)))     # interest_formula = interest
        print(compound)

elif investment_or_bond == 'bond':
    house_present_value = float(input("enter the current value of the house"))
    interest_rate = int(input("enter the interest rate as an integer"))
    number_of_months = int(input("enter the number of months you want to pay your bond"))

    x = (interest_rate * house_present_value)/(1 - (1 + interest_rate) ^ (-number_of_months))
    print(x)     # assigning the formula if the user has entered bond