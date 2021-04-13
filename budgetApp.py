
class budget:
    
    def __init__(self, category):
        self.category = category
        self.balance = 0.0
    
    def displayBalance(self):
        print('Your account balance is: \n', self.balance)

    def deposit(self):
        deposit = int(input('How much do you want to deposit \n'))
        print('%s has been deposited \n' % deposit)
        self.balance = self.balance + deposit
        print('Your new balance is: \n', self.balance)

    def withdraw(self):
        withdraw = int(input('how much do you want to withdraw \n'))
        if self.balance >= withdraw:
            self.balance = self.balance - withdraw
            print('Amount withdrawed is: \n', withdraw)
            print('Your new balance is: \n',self.balance)
        else:
            print('You have insufficient balance \n')
        
    def transferBal(self):
        transferBal = int(input('How much do you want to transfer \n'))
        if self.balance >= transferBal:
            self.balance = self.balance - transferBal
            print('You have successfully transfered: \n', transferBal)
            print('Your new balance is: \n', self.balance)
        else:
            print('You have insufficient balance \n')
    
    
    
food = budget('rice')
clothing = budget('jeans')
entertainment = budget('party')

food.displayBalance()
food.deposit()
food.withdraw()
food.transferBal()

clothing.displayBalance()
clothing.deposit()
clothing.withdraw()
clothing.transferBal()

entertainment.displayBalance()
entertainment.deposit()
entertainment.withdraw()
entertainment.transferBal()
