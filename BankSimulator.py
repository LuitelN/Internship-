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
        u1.deposit(amount)
        u2.deposit(amount)
        u3.deposit(amount)
        u4.deposit(amount)
        u5.deposit(amount)

    elif action == "withdraw":
        amount = float(input("Enter the withdraw amount: "))
        u1.withdraw(amount)
        u2.withdraw(amount)
        u3.withdraw(amount)
        u4.withdraw(amount)
        u5.withdraw(amount)

    else:
      print("Invalid Action")

    print("\nUpdated Account Information:")
    print("Account Holder:", user.name, "\nAccount Number:", user.number, "\nAccount Balance:", user.balance)

else:
    print("User not found.")



    print("Invalid account number.")


        