# FinAid-Loan-Calculator

FinAid-Loan-Calculator is a Python terminal based calculator that computes the monthly payment amount, the total amount of payment upto maturity and the cost of borrowing based on the inputs provided by the user. This program runs on Code Institute mock terminal Heroku. 

The terminal loan calculator enables the users to type in new input values for the principal amount, interest rate and loan duration to find out the corresponding monthly loan payment, the total amount of payment upto maturity and the total cost of borrowing.

[!]The live version of FinAid-Loan-Calculator

## How to use it 

-- The user starts the terminal loan calculator by clicking the Run Proogram button. 

-- the screen displays a welcome message and asks if the user want to calculate a loan. There is a yes or no alternative. If the user type 'no' then it shows a thank you message and ends the program.

-- if the user type 'yes', the loan calculator proceeds. it asks the user to enter the amount to be borrowed, the expected annual interest rate and the duration in years to pay back the loan.

-- after entering the above variables, when the user click enter the monthly amount that should be paid,the total amount paid at the end of the loan period and the coost of borrowing is calculated.

- After getting the resultss, the user will be asked if He/she want to to try again with a different input.


# Features
## Existing Features

- Welcoming message
- Accepts input from the user
- after receiving the input, the monthly amount to be paid, the total amount of loan in a given year and the amortization schedule will be displayed.
- input validation and error checking
    -- the user should enter a numeber otherwise   a warning message will be displayed. 

    -- the user should enter the interest rate in decimal form, to calculate an interest rate of 7%, 0.07 should be entered instead of 7.

## Future features 

--  should allow to plot a graph for different loan scenarios 

-- should provide a user with a feedback 


## Data Model 

--


## Testing 



## Bugs 
The bank will send you a confirmation letter after disbursal of the loan amount either as an email or as a paper copy along with a welcome kit.


## Remaining bugs


## validator testing

 -- PEP8
  --  No errors were found when validating through PEP8online.com.


## Deployment

Thid project is deployed using Code Institute's mock terminal for Heroku. 
    -- steps for deployment 
     - All dependencies were placed in the `requirements.txt` file
     - fork or clone 
     - the buildpacks were set to python and NodeJS
     - two buildpacks from the _Settings_ tab with the ordering 
1. `heroku/python`
2. `heroku/nodejs` were created
      -  a _Config Var_ called `PORT` with Set this to `8000` wrer created 
            . Link the Heroku app to the repository
            . click on deploy
    
Connect your GitHub repository and deploy as normal.

## credits

-  Code Institute for creating the deployment terminal Heroku 
 https://www.geeksforgeeks.org/clear-screen-python/
 https://stackoverflow.com/questions/2084508/clear-terminal-in-python

- 

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.


