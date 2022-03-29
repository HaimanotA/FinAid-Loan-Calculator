import numpy_financial as npf
import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

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
    Get the inputs from the user and calculate monthly installment
    """
    monthly_payment = npf.pmt(r/12, n*12, p)
    print(round(monthly_payment, 2))
print('Monthly Installment Amount (Principal + Interest) is: ')

calculate_amortization_amount(principal, interest_rate, term_in_years)

# calculte the total loan amount

def calculate_total_amount(p, r, n):
    """
    Get the inputs from the user and calculate total loan amount
    """
    total_amount = p * (1 + r/12* n*12)
    print(round(total_amount, 2))
print('Total payment amount (Principal + Interest) is: ')

calculate_total_amount(principal, interest_rate, term_in_years)

# calculate the amortization schedule
per = np.arange(n) + 1
def calculate_amortization_schedule(p, r, n):
    interest_paids = npf.ipmt(r/12, per, n*12, p)
    principal_paids = npf.ppmt(r/12, per, n*12, p)

    fmt1 = '{0:s} {1:s} {2:s} {3:s}'
    fmt2 = '{0:2d} {1:12.2f} {2:15.2f} {3:15.2f}'
    fmt3 = '{0:2d} {1:12.2f} {2:15.2f} {3:15.2f}'

    print(fmt1.format('Term', 'Principal Paid', 'Interest Paid', 'Remaining Principal'))
    print(fmt2.format(0, 0, 0, principal))
    
for x in per:
    i = x - 1
    principal = p + principal_paids[i]
    print(fmt3.format(n*12, principal_paids[i], interest_paids[i], p))

calculate_amortization_schedule(principal, interest_rate, term_in_years)