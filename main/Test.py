import BankStatement
inputAccountHolderName = ''
#Input, Assignment, Validation for the _accountHolderName
while(inputAccountHolderName.isalpha() != True or inputAccountHolderName.isspace() for x in inputAccountHolderName != True ): #Ask user until the input is a valid name (isalpha() and if digit ask them again)
    try:
        inputAccountHolderName = input('Please enter the name of the account holder: ')
        str(inputAccountHolderName) #Input
        if inputAccountHolderName.isdigit(): #Validation
            print('Please enter a valid name')
            continue   
    except ValueError:
        print('Please enter a valid name')
