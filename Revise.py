class User: 
    def __init__(self, First_Name,Last_Name, Account_Number, Balance):
        self.Fname = First_Name
        self.Lname = Last_Name
        self.number = Account_Number
        self.balance = Balance 

acc_holders = {}
UserBase = int(input("Enter the number of users: "))
for i in range(UserBase):
    key = input("Enter the first name: ")
    value = input("Enter the last name: ")
    acc_holders[key] = value 
    print("The users are: ")
    print(acc_holders)



