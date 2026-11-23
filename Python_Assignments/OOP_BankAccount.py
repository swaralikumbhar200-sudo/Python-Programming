#Write a Python program to implement a class named BankAccount with the following requirements:
#1.The class should contain two instance variables:
     #1.Name (Account holder name)
     #2.Amount (Account balance)
# 2.The class should contain one class variable:
     #1.ROI (Rate of Interest), initialized to 10.5
#3.Define a constructor (__init__) that accepts Name and initial Amount.
#4.Implement the following instance methods:
#1.Display()
#Displays the account holder name and current balance.
#2.Deposit()
#Accepts an amount from the user and adds it to the balance.
#3.Withdraw()
#Accepts an amount from the user and subtracts it from the balance.
#(Ensure withdrawal is allowed only if sufficient balance exists.)
#4.CalculateInterest()
#Calculates and returns interest using the formula:
#Interest = (Amount * ROI) / 100
#Create multiple objects and demonstrate all methods.


class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder name: ",self.Name)
        print("Current balance: ", self.Amount)

    def Deposit(self):
        money =float(input("Enter an amount: ")) 
        self.Amount =self.Amount + money
        print("Amount Deposited Successfully")

    def Withdraw(self):
        money = float(input("Enter amount to withdraw: "))

        if money <= self.Amount:
            self.Amount = self.Amount - money
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

Obj1 = BankAccount("Rahul", 10000)

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()

print("Interest =", Obj1.CalculateInterest())
Obj1.Display()

print("----------------------------")

Obj2 = BankAccount("Priya", 5000)

Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()

print("Interest =", Obj2.CalculateInterest())
Obj2.Display()

    



        