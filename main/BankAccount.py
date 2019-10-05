class BankAccount:
    def __init__(self):
        _bankaccountNumber = 0
        _initialBalance = 0
        _interestRate = 0.3
        _accountHolderName = ''
        _monthlyDeposit = 0
        _monthlyWithdrawal = 0

    def bankProgram(self):
        display = 'Welcome to Programming Principles Bank' #Start of bankProgram menu
        print(display) #Printing out bankProgram menu
        #Declaring inputValues for attributes
        inputAccountHolderName = '' #Initializing inputAccountHolderName variable
        inputAccountNumber = '' #Initializing inputAccountNumber variable
        inputAnnualInterestRate = '' #Intializing inputAnnualInterestRate variable
        inputInitialBalance = '' #Intializing inputInitialBalance variable
        inputMonthlyDeposit = '' #Intializing inputMonthlyDeposit variable
        inputMonthlyWithdrawal = '' #Intializing inputMonthlyWithdrawal
        bankInformationSubmitted = False
        try:
            while(bankInformationSubmitted != True): #Ask user all of information until the user reaches to the end
                #Input, Assignment, Validation for the _accountHolderName
                while(inputAccountHolderName.isalpha() != True): #Ask user until the input is a valid name (isalpha() and if digit ask them again)
                    try:
                        inputAccountHolderName = input('Please enter the name of the account holder: ') #Input
                        if inputAccountHolderName.isdigit(): #Validation
                            print('Please enter a valid name')
                            continue   
                    except ValueError:
                        print('Please enter a valid name')
                self._accountHolderName = inputAccountHolderName.capitalize() #Assignment of _accountHolderName, Capitalize the first letter of the user name
                #Input, Assignment, Validation for the _accountNumber
                while(inputAccountNumber.isdigit() != True or int(inputAccountNumber) < 100 or int(inputAccountNumber) > 1000):
                    try:
                        inputAccountNumber = input('Please enter the account number: ') #Input
                        if inputAccountNumber.isalpha() or int(inputAccountNumber) < 100 or int(inputAccountNumber) > 1000 : #Validation
                            print('Please enter a valid account number')
                            continue
                    except ValueError:
                        print('Please enter a valid account number')
                self._bankAccountNumber = inputAccountNumber  #Assignment of _accountHolderName, Capitalize the first letter of the user name
                #Input, Assignment, Validation for the _accountAnnualInterestRate
                inputAnnualInterestRate = input('Please enter the annual interest rate percentage: ')
                self._interestRate = inputAnnualInterestRate  
                inputInitialBalance = input('Please enter the initial balance: ')
                self._initialBalance = inputInitialBalance  
                inputMonthlyDeposit = input('Please enter the monthly deposit: ')
                self._MonthlyDeposit = inputMonthlyDeposit  
                inputMonthlyWithdrawal = input('Please enter the monthly withdrawal: ')
                self._monthlyWithdrawal = inputMonthlyWithdrawal  
                bankInformationSubmitted = True
        except:
            print('Something wrong has happened here...')
    
    #This method will be responsible for the print of the _bankAccountNumber, _accountHolderName,
    #def displayBankStatement ():
    