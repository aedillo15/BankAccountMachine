import BankAccount
inputAccountHolderName = ''
while (inputAccountHolderName.isalpha() != True):
    try:
        inputAccountHolderName = input('Please enter the name of the account holder: ') 
        if inputAccountHolderName.isdigit():
            print('Please enter a valid name')
            continue   
    except ValueError:
        print('Please enter a valid name')