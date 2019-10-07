import BankStatement
#Tested: Input Bank Holder Name, Input Account Number

#Testing: Input Annual Interest Rate, Initial Balance, Monthly Deposit, Monthly Withrawal
inputMonthlyDeposit = ''
while(type(inputMonthlyDeposit) != float): # While loop until the inputInitialBalance is equal to a float
    inputMonthlyDeposit = input('Please enter the initial balance [>= 0]: ')
    if inputMonthlyDeposit.isalpha() == True:#Validate that inputIntialBalance is not alphabetical
        print('Please enter a valid balance that is numeric.')
    inputMonthlyDeposit = float(inputMonthlyDeposit)     
    if inputMonthlyDeposit <= 0:  #Validate that inputInitialBalance less than or equal to 0
        print('Please enter a valid balance greater than 0.')
