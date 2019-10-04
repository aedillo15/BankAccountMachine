class BankAccount:
    def __init__(self):
        _bankaccountNumber = 0
        _initialBalance = 0
        _interestRate = 0.3
        _accountHolderName = ''
        _monthlyDeposit = 0
        _monthlyWithdrawal = 0

    def bankProgram(self):
        display = 'Welcome to Programming Principles Bank'
        print(display)
        bankInformationSubmitted = False
        try:
            while(bankInformationSubmitted != True):
                inputAccountHolderName = input('Please enter the name of hte account holder: ')
                self._accountHolderName = inputAccountHolderName  
                inputAccountNumber = input('Please enter the account number: ')
                self._bankAccountNumber = inputAccountNumber 
                inputAnnualInterestRate = input('Please enter the annual interest rate percentage: ')
                self._interestRate = inputAnnualInterestRate  
                inputInitialBalance = input('Please enter the initial balance: ')
                self._initialBalance = inputInitialBalance  
                inputMonthlyDeposit = input('Please enter the monthly deposit: ')
                self._MonthlyDeposit = inputMonthlyDeposit  
                inputMonthlyWithdrawal = input('Please enter the monthly withdrawal: ')
                self._monthlyWithdrawal = inputMonthlyWithdrawal  
                bankInformationSubmitted = True
        except():
            print('Something wrong has happened here...')
    