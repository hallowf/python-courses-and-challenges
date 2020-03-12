from __future__ import print_function, division
try:
  input = raw_input
except NameError:
  pass

### Formula
# M = L[i(1+i)n] / [(1+i)n-1]

# M = Monthly payment
# L = Loan amount
# i = interest rate (for an interest rate of 5%, i = 0.05)
# n = number of payments

loan_amount = input("Enter the loan amount ")
interest_rate = input("Enter the interest rate ")
loan_years = input("Enter the loan years ")
loan_amount = int(loan_amount)
print("Loan amount: %d" % loan_amount)
interest_rate = float(interest_rate)
interest_rate = interest_rate / 100
print("Interest rate: %.2f" % interest_rate)
loan_years = int(loan_years)
print("Loan years: %d" % loan_years)

number_of_payments = loan_years * 12

# TODO: This seems to be correct  according to the formula
#  however the output value is far lower than expected
monthly_pay = loan_amount * (interest_rate * (1+interest_rate) * number_of_payments) \
  / ((1+interest_rate) * number_of_payments-1)

print("The monthly pay is %f" % monthly_pay)