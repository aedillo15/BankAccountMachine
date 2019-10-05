import BankStatement
#Tested: Input Bank Holder Name, Input Account Number

#Testing: Input Annual Interest Rate, Initial Balance, Monthly Deposit, Monthly Withrawal
inputAnnualInterestRate = ''
while(type(inputAnnualInterestRate) != float): #While the inputOfAnnualInterest is a float
    inputAnnualInterestRate = input('Please enter the annual interest rate percentage [> 0]: ')
    if inputAnnualInterestRate.isalpha() or int(inputAnnualInterestRate) < 0: #Validate that inputAnnualInterestRate is not alphabetical and less than 100
        print('Please enter a valid annual interest rate.')
    inputAnnualInterestRate = int(inputAnnualInterestRate) / 100 #Turn the whole number into a percentage by dividing the inputAnnualInterestRate by 100
    float(inputAnnualInterestRate)
