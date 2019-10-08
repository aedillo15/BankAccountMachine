import BankStatement
#Tested: Input Bank Holder Name, Input Account Number

#Testing: Input Annual Interest Rate, Initial Balance, Monthly Deposit, Monthly Withrawal
inputMonthlyWithdrawal = ''
while(type(inputMonthlyWithdrawal) != float): # While loop until the inputInitialBalance is equal to a float
    inputMonthlyWithdrawal = input('Please enter the monthly withdrawal [< 1000]: ')
    if inputMonthlyWithdrawal.isalpha() == True:#Validate that inputIntialBalance is not alphabetical
        print('Please enter a valid balance that is numeric.')  
    if float(inputMonthlyWithdrawal) < 100:  #Validate that inputInitialBalance less than or equal to 0
        print('Please enter a valid balance greater than 100.')
    if float(inputMonthlyWithdrawal) >= 100:
        inputMonthlyWithdrawal = float(inputMonthlyWithdrawal) 