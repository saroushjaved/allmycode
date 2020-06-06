# This program is aimed to help you calculate the number of months you need
# to save for your house

total_cost = float(input(" Enter the worth of your dream house "))
annual_salary = float(input( " Enter you annual salary : "))
down_payment = float(input(" Enter percentage of down payment (0-1) : " ) )
semi_annual_raise = float(input( " Enter your semi annual raise (0-1) : " ))
current_savings = 0
saving_percentage = float(input("Enter your saving percentage"))
i_rate= 0.04
time = 0.0


while current_savings <= (total_cost* down_payment):
    
    monthly_salary = annual_salary/12

    current_savings = current_savings + ( ( monthly_salary * saving_percentage) + (( current_savings*i_rate)/12))
    time = time + 1

    if (time % 6) == 0:
        annual_salary = annual_salary * ( 1 + semi_annual_raise )
    
        
print(time)
