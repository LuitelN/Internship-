class User: 
    def __init__(self, Name, Account_Number, Balance):
        self.name = Name 
        self.number = Account_Number
        self.balance = Balance 

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited."
              )
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance.")
        else: 
            self.balance -= amount
            print(f"{amount} withdrawn.")



u1 = User("A", 1 , 10000 )
u2 = User("B", 2 , 20000 )
u3 = User("C", 3 , 40000 )
u4 = User("D", 4 , 50000 )
u5 = User("E", 5 , 15000 )

accounts = {1: u1, 2: u2, 3: u3, 4: u4, 5: u5}

result = int(input("Enter the account number: "))
user = accounts.get(result)


#print(accounts.items())
#dict: key, values,items, get, read, update, create

if user: 
    print("Account Holder:", user.name, "\nAccount Number:", user.number, "\nAccount Balance: ", user.balance)
    action = input("Do you want to Deposit or Withdraw?")

    if action == "deposit":
        amount = float(input("Enter the deposit amount: "))
        user.deposit(amount)

    elif action == "withdraw":
        amount = float(input("Enter the withdraw amount: "))
        user.withdraw(amount)

else:
    print("Invalid Action")

    print("\nUpdated Account Information:")
    print("Account Holder:", user.name, "\nAccount Number:", user.number, "\nAccount Balance:", user.balance)





# print("Account Holder:", u1.name, "\nAccount Number:", u1.number, "\nAccount Balance: ", u1.balance)
# print("Account Holder:", u2.name, "\nAccount Number:", u2.number, "\nAccount Balance: ", u2.balance)
# print("Account Holder:", u3.name, "\nAccount Number:", u3.number, "\nAccount Balance: ", u3.balance)
# print("Account Holder:", u4.name, "\nAccount Number:", u4.number, "\nAccount Balance: ", u4.balance)
# print("Account Holder:", u5.name, "\nAccount Number:", u5.number, "\nAccount Balance: ", u5.balance)


        