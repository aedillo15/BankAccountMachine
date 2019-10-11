from BankStatement import BankStatement
class Program:
    def __init__(self):
        #Create a BankAccount object then call the function created inside of the object
        self._BankStatement1 = BankStatement()

prog = Program()        
#Call the method from BankStatement which is the bankProgram() method
prog._BankStatement1.bankProgram()
#After the bankProgram() method which is responsible for assigning the field variables of BankStatement object
prog._BankStatement1.displayBankStatement()


