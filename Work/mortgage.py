# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months = months + 1
    new_payment = payment

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        new_payment = payment + extra_payment

    current_principal = principal * (1 + rate / 12)
    if current_principal < new_payment:
        new_payment = current_principal

    principal = current_principal - new_payment
    total_paid = total_paid + new_payment
    print(months, round(total_paid, 2), round(principal, 2))


print("Total paid", total_paid, " over ", months)
