class atm:
    def __init__(self, cardNumber,pinNumber,bankBalance,withDrawalAmt,depositAmt):
        self.cardNumber = int(cardNumber)
        self.pinNumber = int(pinNumber)
        self.bankBalance = int(bankBalance)
        self.withDrawalAmt = int(withDrawalAmt)
        self.depositAmt = int(depositAmt)
        #self.newBankBalance = int(newBankBalance)

    def inputCard(self):
        self.cardNumber = int(input("Enter card number "))
    
    def inputPin(self):
        self.pinNumber = int(input("Enter pin number"))
    
    def inputBankBalance(self):
        self.bankBalance = int(input("Enter your bank balance"))

    def inputWithdrawal(self):
        self.withDrawalAmt = int(input("Enter withdrawal amount"))
        self.bankBalance = self.bankBalance - self.withDrawalAmt 
    
    def inputDeposit(self):
        self.depositAmt = int(input("Enter deposit amount"))
        self.bankBalance = self.bankBalance + self.depositAmt
    
    def newBankBalance(self):
        print(self.bankBalance)





acc1 = atm(0,0,0,0,0)

acc1.inputCard()
acc1.inputPin()
acc1.inputBankBalance()
choice = str(input("Enter deposit or withdrawal"))
if choice == "withdrawal":
    acc1.inputWithdrawal()
    
else:
    acc1.inputDeposit()

print("Card Number: "+str(acc1.cardNumber))
print("Pin Number: "+str(acc1.pinNumber))
print("Bank Balance: "+str(acc1.bankBalance))
