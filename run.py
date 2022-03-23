import numpy_financial as npf
# Loan calculator and amortization schedule
principal = int(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate amount: "))
term_in_years = int(input("Enter term in years: "))
# initiation_date = input ("Enter initiation date: ")

# print(principal)
# print(interest_rate)
# print(term_in_years)
# print(initiation_date)


# p the principal amount
# r interest rate
# number of years


def calculate_amortization_amount(p, r, n):
    amt = npf.pmt(r/12, n*12, p)
    print(round(amt, 2))


calculate_amortization_amount(principal, interest_rate, term_in_years)
