# User input for Financial Details
m_income = int(input("Enter your monthly income: "))
t_expense = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Saving
m_savings = m_income - t_expense

# Projected Annual Saving
annual_rate = 0.05
projected_saving = m_savings * 12 + (m_savings * 12 * annual_rate)

print("Your monthly savings are ${}.".format(m_savings))
print("Projected savings after one year, with interest, is: ${:.0f}.".format(projected_saving))