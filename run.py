import numpy_financial as npf
# Take input from the user to calculate the monthly repayment for a loan

principal = int(input("Enter the principal amount:\n"))

interest_rate = float(input("Enter interest rate amount in decimal:\n"))

term_in_years = int(input("Enter term in years:\n"))
# initiation_date = input ("Enter initiation date: ")

# defining the terms 
# p is the principal amount of money borrowed
# r is the annual interest rate
# n is the number of years

# calculate the monthly installment amount

def calculate_amortization_amount(p, r, n):
    """
    Get loan figures input from the user
    """
    amt = npf.pmt(r/12, n*12, p)
    print(round(amt, 2))
print('Monthly Installment Amount (Principal + Interest) is: ')

calculate_amortization_amount(principal, interest_rate, term_in_years)

# calculte the total loan amount

def calculate_total_amount(p, r, n):
    """
    Get loan figures input from the user
    """
    amount = p * (1 + r/12* n*12)
    print(round(amount, 2))
print('Total payment amount (Principal + Interest) is: ')

calculate_total_amount(principal, interest_rate, term_in_years)
