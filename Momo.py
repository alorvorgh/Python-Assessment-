import random
class momo:
    def __init__(self, amount ,max_withdrawal,amount_today,withdrawals_today,limit_a_day):
        self.balance = amount
        self.max_withdrawal = max_withdrawal
        self.amount_today = amount_today
        self.withdrawals_today = withdrawals_today
        self.limit_a_day = limit_a_day
  

    def deposit(self):
        self.balance += amount
        
    def withdraw(self):
        self.balance -= amount
        
    def getbalance(self):
        return self.balance

def main():
    min_balance = 1000

    id = int(input("\nEnter your mobile number: "))
    while(True):
        print("\nMenu \n1. Deposit Cash \n2. Withdraw Cash \n3. Check Balance \n4. Exit")
        option = int(input("\nEnter your selection: "))

            #Deposit
        if option == 1:
            amount = float(input("Please enter an amount to deposit: "))
            min_balance = amount + min_balance
            print('Cash In received for GHS{}. \nCurrent Balance: GHS{}'.format(amount,min_balance))

        #withdrawal
        elif option == 2:
            max_withdrawal = 2000
            limit_a_day = 4
            withdrawals_today = 0 + 1
            amount = float(input("Please enter an amount to withdraw: "))
            amount_today = 0 + amount
            zadok = momo( amount, 2000, amount_today, withdrawals_today, 4)
            new_balance = min_balance - zadok.getbalance()
            print('Cash Out made of GHS{}. \nCurrent balance is GHS{}'.format(amount,new_balance))
            
            can_withdraw = False
            if amount > zadok.getbalance():
                print("Sorry, You have insufficient funds in your account.")
                print("Please enter a valid amount")
                
            can_withdraw = False
            if zadok.getbalance()> max_withdrawal:
                print("Sorry, You cannot make a withdrawal greater than GHc2000.")
                
            can_withdraw = False
            if amount + amount_today >= max_withdrawal:
                print("Sorry, You have reached the maximum amount you can withdraw today.")
                
            can_withdraw = False
            if withdrawals_today >= limit_a_day:
                print("Sorry, You cannot make anymore withdrawals today.")
                
            else:
                withdrawals_today += 1
                amount_today += amount
                new_balance = min_balance - zadok.getbalance()
 
        elif option == 3:
            print('Your avalaiable balance: GHS{} '.format(min_balance))
            
        elif option == 4:
            print("Transaction is now complete.")
            print("Transaction number : ", random.randint(10000, 100000))
            print("Thanks you")
            exit()
            
                
main()
