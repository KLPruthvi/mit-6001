intial_salary = float(input("Enter the starting salary : "))
semi_annual_raise = 0.07
annual_return = 0.04
cost_of_the_house = 1000000
down_payment = 0.25 * cost_of_the_house
total_months = 36
epsilon = 100 #margin of error

num_guesses = 0
low = 0
high = 10000 # to make the decimal math easy
guess = (high + low)// 2 # to chop off the decimals and to keep whole number
while True: #creating an infinite loop until we say break
    rate = guess / 10000 #for conversion purpose
    current_savings = 0 # resetting the values, the most important lines
    annual_salary = intial_salary # resetting the values, the most important lines
    monthly_salary = annual_salary / 12 # resetting the values, the most important lines
    for month in range(36): # since we know how many months, (range)
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * rate
        
        if (month + 1) % 6 == 0: # modular checks if reminder is 0
            annual_salary += annual_salary * semi_annual_raise # updating the amounts
            monthly_salary = annual_salary / 12
    if abs(current_savings - down_payment) <= epsilon:
        print("best savings rate: ", rate)
        print("steps in bisection search: ", num_guesses)
        break
    if high - low <= 1:
        print("not possible in three years.")
        break
    if current_savings > down_payment:
        high = guess
    else: 
        low = guess
    guess = (high + low)// 2 #performs floow division
    num_guesses += 1