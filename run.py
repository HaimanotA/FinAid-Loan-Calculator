import numpy_financial as npf
import numpy as np
import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# defining the terms
# p (pricipal) = amount of money borrowed
# r (interest rate) = annual interest rate
# t (time_in_years) = duration of the loan until it is paid off
# Take input from the user to calculate the monthly repayment for a loan

clear()


def get_principal():
    principal = input("Enter the principal amount:\n")
    try:
        p = int(principal)
        clear()
        get_interest(p)
    except ValueError:
        clear()
        print('Sorry that is not a valid option!')
        get_principal()


def get_interest(p):
    interest_rate = input("Enter interest rate amount in decimal:\n")
    try:
        r = float(interest_rate)
        clear()
        get_term_in_years(p, r)
    except ValueError:
        clear()
        print('Sorry that is not a valid option!')
        get_interest(p)


def get_term_in_years(p, r):
    term_in_years = input("Enter term in years:\n")
    try:
        n = int(term_in_years)
        clear()
        calculate_amortization_amount(p, r, n)
    except ValueError:
        clear()
        print('Sorry that is not a valid option!')
        get_term_in_years(p, r)


def calculate_amortization_amount(p, r, n):
    """
    Get the inputs from the user and calculate monthly installment
    """
    clear()
    monthly_payment = npf.pmt(r/12, n*12, p)
    payment = round(monthly_payment, 2)
    print(f'The principal amount is {p}')
    print(f'The annual interest rate is {r}')
    print(f'The time period is {n} years\n')

    print(f'Monthly Installment Amount is {payment}')
    print('This amount includes principal and interest.\n')
    calculate_total_amount(p, r, n)


# calculte the total loan amount
def calculate_total_amount(p, r, n):
    """
    Get the inputs from the user and calculate total loan amount
    """
    total_amount = p * (1 + r / 12 * n*12)
    total = round(total_amount, 2)
    print(f'Total amount of loan at the end is {total}')
    print('This amount includes principal and interest\n')
    calculate_cost_of_borrowing(total_amount, p)


# calculate the difference between amount paid and borrowed
def calculate_cost_of_borrowing(total_amount, p):
    """
    calculate the total cost of loan
    """
    cost_of_borrowing = total_amount - p
    cost = round(cost_of_borrowing, 2)
    print(f'The cost of borrowing is {cost}')


def start_calculation():
    while True:
        answer = input(
            '\Welcome to FinAid-Loan-Calculator!\n'
            '\nDo you want to calculate your loan? yes/no\n')
        if answer.lower() != 'yes':
            break
        else:
            clear()
            get_principal()
    clear()
    print('Thank you for visiting!')


start_calculation()
