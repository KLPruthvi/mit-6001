intial_salary = float(input("Enter the starting salary : "))
semi_annual_raise = 0.07
annual_return = 0.04
cost_of_the_house = 1000000
down_payment = 0.25 * cost_of_the_house
total_months = 36
epsilon = 100 #target range

num_guesses = 0
low = 0
high = 10000 # to make the decimal math easy
guess = (high + low)// 2 # to chop off the decimals and to keep whole number
while True:
    rate = guess / 10000
    current_savings = 0
    annual_salary = intial_salary
    monthly_salary = annual_salary / 12
    for month in range(36):
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * rate
        
        if (month + 1) % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    if abs(current_savings - down_payment) <= epsilon:
        print("best savings rate: ", rate)
        print("steps in bisection search: ", num_guesses)
        break
    if low >= high :
        print("not possible in three years.")
        break
    if current_savings > down_payment:
        high = guess
    else: 
        low = guess
    guess = (high + low)// 2
    num_guesses += 1