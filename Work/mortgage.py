# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    if total_months < 12:
        principal = principal - 1000
    total_months = total_months + 1
    total_paid = total_paid + payment


print("Total paid", total_paid, " over ", total_months)
