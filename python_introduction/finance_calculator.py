Monthly_income = int(input('Enter your monthly income: '))
Monthly_expenses = int(input('Enter your total monthly expenses: '))
simple_annual_interest = 0.05

Monthly_savings = Monthly_income - Monthly_expenses
print (Monthly_savings)

Projected_Savings = Monthly_savings * 12 + Monthly_savings * 12 * 0.05
print (Projected_Savings)