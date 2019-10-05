import BankAccount

inputAccountNumber = ''
while(inputAccountNumber.isdigit() != True or int(inputAccountNumber) < 100 or int(inputAccountNumber) > 1000):
    try:
        inputAccountNumber = input('Please enter the account number: ') #Input
        if inputAccountNumber.isalpha() or int(inputAccountNumber) < 100 or int(inputAccountNumber) > 1000 : #Validation
            print('Please enter a valid account number')
            continue
    except ValueError:
        print('Please enter a valid account number')