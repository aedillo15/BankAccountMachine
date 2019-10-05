class BankStatement: #BankStatement class declaration
    def __init__(self): #BankStatement constructor
        _accountNumber = 0 #accountNumber for the BankStatement class
        _initialBalance = 0 #intialBalance for the BankStatement class
        _interestRate = 0.3 #interestRate for the BankStatement class
        _accountHolderName = '' #accountHoldername for the BankStatement class
        _monthlyDeposit = 0 #monthlyDeposit for the BankStatment class
        _monthlyWithdrawal = 0 #monthlyWithdrawal for the BankStatement class
    def bankProgram(self):  #bankProgram() is responsible for the input, assignment and validation of attributes the BankStatement 
        display = 'Welcome to Programming Principles Bank' #Start of bankProgram menu
        print(display) #Printing out bankProgram menu
        #Declaring inputValues for attributes
        inputAccountHolderName = '' #Initializing inputAccountHolderName variable
        inputAccountNumber = '' #Initializing inputAccountNumber variable
        inputAnnualInterestRate = '' #Intializing inputAnnualInterestRate variable
        inputInitialBalance = '' #Intializing inputInitialBalance variable
        inputMonthlyDeposit = '' #Intializing inputMonthlyDeposit variable
        inputMonthlyWithdrawal = '' #Intializing inputMonthlyWithdrawal
        bankInformationSubmitted = False #Initializing boolean for while loop information
        try:
            while(bankInformationSubmitted != True): #Ask user all of information until the user reaches to the end
                #Input, Assignment, Validation for the _accountHolderName
                while(inputAccountHolderName.isalpha() != True ): #Ask user until the input is a valid name (isalpha() and if digit ask them again)
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
                self._accountNumber = inputAccountNumber  #Assignment of _accountNumber
                #Input, Assignment, Validation for the _accountAnnualInterestRate
                while(inputAnnualInterestRate.isdigit() != True):
                    inputAnnualInterestRate = input('Please enter the annual interest rate percentage(%): ')
                    if inputAnnualInterestRate.isalpha() or int(inputAnnualInterestRate) < 100: #Validate that inputAnnualInterestRate is not alphabetical and less than 100
                        print('Please enter a valid annual interest rate.')
                    inputAnnualInterestRate = inputAnnualInterestRate / 100 #Turn the whole number into a percentage by dividing the inputAnnualInterestRate by 100
                self._interestRate = inputAnnualInterestRate #Assignment of _interestRate to the inputAnnualInterestRate of the user 
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
    