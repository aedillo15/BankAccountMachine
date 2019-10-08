import BankStatement
#Tested: Input Bank Holder Name, Input Account Number

#Testing: Input Annual Interest Rate, Initial Balance, Monthly Deposit, Monthly Withrawal
Name = ''
_accountHolderName = ''
inputAccountHolderName = ''
while(Name.isalpha() != True ): #Ask user until the input is a valid name (isalpha() and if digit ask them again)
    try:
        inputAccountHolderName = input('Please enter the name of the account holder: ') #Input
        if inputAccountHolderName.isdigit(): #Validation
            print('Please enter a valid name')
            continue   
        splitName = inputAccountHolderName.split() #Split the inputAccountHolderName
        firstName = splitName[0] #Assign the firstName to the 0 index of the splitName list
        _accountHolderName = firstName
        Name = firstName #Name is equal to the firstName
        print(_accountHolderName)
        if(len(splitName) == 2): #Yet, if the length of it is 0-1 then it is going to be a lastName 
            lastName = splitName[1] #Assign the lastName to the splitName 2nd index
            Name += lastName.capitalize() #Concatanate this name to the Name as a condition to get out of the while loop
            _accountHolderName = firstName + ' ' + lastName
            print(_accountHolderName)
    except ValueError: #If there are any ValueErrors be able to handle it
        print('Please enter a valid name')