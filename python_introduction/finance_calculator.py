# User input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Saving
monthly_savings = monthly_income - monthly_expenses

# Projected Annual Saving
annual_rate = 0.05
projected_saving = monthly_savings * 12 + (monthly_savings * 12 * annual_rate)

print("Your monthly savings are ${}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${:.0f}.".format(projected_saving))