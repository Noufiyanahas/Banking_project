#Write a python program to replicate a Banking system. The following features are mandatory:
#1.Account login
#2. Amount Depositing
#3. Amount Withdrawal

class Bank_account:
    amount=1000
    flag=0
    dict1={"zara":1234,"nooha":4567,"ram":3456}
    def login(self):
            self.name=input("enter username: ")
            self.acnt_num = int(input("enter your account number: "))
            if (self.acnt_num in self.dict1.values()) & (self.name in self.dict1.keys()):
               print("welcome",self.name)
               self.flag=1
               return self.flag
            else:
               print("invalid username and account number")
    def deposit(self):
      if self.flag==1:
        self.deposit_amount=int(input("enter amount to be deposit: "))
        self.amount=self.amount + self.deposit_amount
        print("Amount successfully deposited")
    def withdraw(self):
      if self.flag==1:
        self.withdraw_amount = int(input("enter amount to be withdrawn: "))
        if self.amount>self.withdraw_amount:
            self.amount = self.amount - self.withdraw_amount
            print("Amount successfully withdrawn")
        else:
            print("insufficient balance")
    def get_balance(self):
        if self.flag==1:
           print("your bank balance is",self.amount)
accnt=Bank_account()
accnt.login()
for i in range(1,10):
   print("1.deposit\n2.withdraw\n3.balance\n4.exit")
   choice = int(input("enter your choice"))
   if choice==1:
      accnt.deposit()
   elif choice==2:
      accnt.withdraw()
   elif choice==3:
      accnt.get_balance()
   elif choice==4:
      break