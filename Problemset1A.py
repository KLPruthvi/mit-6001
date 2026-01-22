total_cost = float(input("Total cost of your dream home :"))
annual_salary = float(input("What is your starting annual income :"))
portion_saved = float(input("Portion of your annual salary to be saved :"))

'''monthly_salary = annual_salary / 12
current_savings =  0
portion_down_payment = 0.25 * total_cost
months = 0 # initialize month counter
r = 0.04 #annual interest rate
while current_savings < portion_down_payment :
    investment_returns = current_savings * (r/12) # calculating the investment returns
    monthly_contribution = portion_saved * monthly_salary # monthly we are earning
    current_savings = current_savings + investment_returns + monthly_contribution
    months = months + 1
print("Number of months :", months)'''

semi_annual_raise = float(input("percentage of hike: "))
monthly_salary = annual_salary / 12
current_savings =  0
portion_down_payment = 0.25 * total_cost
months = 0 # initialize month counter
r = 0.04 #annual interest rate
while current_savings < portion_down_payment :
    investment_returns = current_savings * (r/12) # calculating the investment returns
    monthly_contribution = portion_saved * monthly_salary # monthly we are earning
    current_savings = current_savings + investment_returns + monthly_contribution
    months = months + 1
    if months % 6 == 0: # to see if reminder is 0
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        monthly_salary = annual_salary / 12
print("Number of months :", months)



    
    




