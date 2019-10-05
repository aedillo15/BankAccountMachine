import BankStatement
inputAccountHolderName = ''
splitName = ''
Name = ''
#Input, Assignment, Validation for the _accountHolderName
while(Name.isalpha() != True): #Ask user until the input is a valid name (isalpha() and if digit ask them again)
    try:
        inputAccountHolderName = input('Please enter the name of the account holder: ')
        if inputAccountHolderName.isdigit(): #Validation
            print('Please enter a valid name')
            continue   
        splitName = inputAccountHolderName.split() #Input
        firstName = splitName[0]
        Name = firstName
        if(len(splitName) == 2):
            lastName = splitName[1]
            Name += lastName
    
    except ValueError:
        print('Please enter a valid name')
