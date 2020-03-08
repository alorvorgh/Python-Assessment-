Min_Deposit = 500
Login_Attempts = 3

accounts = {
    "5433":{'name':'Kofi','balance':120,'pin':5433},
    "5443":{'name':'Qwame','balance':80,'pin':5443},
    "5453":{'name':'Joshua','balance':190,'pin':5453},
    "5463":{'name':'Karl','balance':75,'pin':5463},
    "5473":{'name':'Zadok','balance':370,'pin':5473}
    }
transactions = {}

logged_in = False
for i in range(Login_Attempts):
    login = input("Enter your Account number: ")
    pin = input("Enter your pin: ")
    account = accounts.get(login)
    if not(account is None):
        pin = account.get('pin')
        name = account.get('name')
        logged_in = True
        print("\nWelcome Mr. {}".format(name))
        break
    else:
        print("Invalid account number and pin.\n Please Try Again\n")
        
def get_transactions(account_no):
    trans = transactions.get(account_no)
    if (trans):
        for item in trans:
            print("Type : {} , Previous Balance : {} , Current Balance : {} "\
                  .format(item.get("type"),item.get("previous_balance"),item.get
                          ("new_balance")))
            
    else:
        print("No transactions have been made for the specified account number")

def menu():
    print("\n1 - Deposit    \t2 - Withdrawal   \t3 - View Balance   \t4 - View Transactions     \t5 - Exit")
    x = input("Please select an action to be performed: ")

    return x

while(logged_in):
    action = menu()
    if action == "1":
        amount = float(input("Please Enter an amount to Deposit: " ))
        print("Your account has been credited with GHc{} ".format(amount))
        balance = account.get("balance")
        new_balance = balance + amount
        print("Updated Balance: GHC{} ".format(new_balance))
        trans = {
            "type":"Deposit", "amount":amount, "previous_balance":balance,"new_balance":new_balance}
        if not (transactions.get(login) is None):
            transactions.get(login).append(trans)
        else:
            transactions[login] = [trans]

    elif action == "2":
        amount = float(input("Please Enter an amount to Withdraw: "))
        print("Your account has been credited with GHc{} ".format(amount))
        balance = account.get("balance")
        new_balance = balance - amount
        print("Updated Balance: GHC{} ".format(new_balance))
        trans = {
            "type":"Withdrawal", "amount":amount, "previous_balance":balance,"new_balance":new_balance}
        if not (transactions.get(login) is None):
            transactions.get(login).append(trans)
        else:
            transactions[login] = [trans]
            
    elif action == "3":
        balance = account.get("new_balance")       
        print("Available Balance: GHC{}".format(new_balance))
        
    elif action == "4":
        print(get_transactions(login))

    elif action == "5":
        print("Transaction is now complete.")
        print("Thanks for choosing us as your bank")
        break
    
    
