#Personal Finance Calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter yourr total monthly expenses: "))
#Calculate mothly savings
monthly_income = 5000 #In  dollars
monthly_expenses = 4000
monthly_savings = monthly_income - monthly_expenses

#PProjecting Annual Savings
interest = 0.05
Projected_Savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#Output
print("Your monthly savings are", monthly_savings)
print("Projected Savings after one year, with interest, is: ", Projected_Savings)

