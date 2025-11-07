
investment = float(input("Investment (baht/rai): "))
production = float(input("Rice production (kg/rai): "))
wholesale = float(input("Wholesale price (baht/kwian): "))

income = production * (1.0 / 1000) * wholesale
balance = income - investment

sheet = "Balance = income ({:,.2f}) - investment ({:,.2f}) = {:,.2f} baht/rai"
print(sheet.format(income, investment, balance))
