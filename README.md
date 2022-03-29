# FinAid-Loan-Calculator

FinAid-Loan-Calculator is a Python command-line project, which runs in the Code Institute mock terminal on Heroku. 

Users are asked to enter an input on the principal amount, the yearly interst rate and the time they would like to take loan for. Then when the user click enter, the monthly payment amount that should be paid and the total amount of loan including the prinicpal and the interest rate will be displayed. 

## How to use it 

- after getting the resultss, the user will be asked to try again with a different input


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
- 

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.


