import random

class BankAccount:
    def __init__ (self,):
       
       self._name = ''
       self._account_number = 0
       self.balance = random.randint(1,5000)
    
    
    
    
    def deposit(self):
        while True: 
            amount = input("How much would you like to deposit? Type 'back' to go back to the menu\n")
            
            try:
           
                user_choice = float(amount)
                
                if user_choice <= 0:
                        print ("Try adding a positive number\n")
                    
                elif user_choice > 0:
                    error_check = input(f"you would like to add ${user_choice}?(Yes/No)\n").lower().strip()
                        
                    if error_check == "no":
                        continue
                        
                    elif error_check == "yes":
                        print (f"Adding {user_choice} to {self.balance} your new balance is {user_choice + self.balance}")
                        self.balance += user_choice
                        break    
            except ValueError:
                amount == "back"
                break

    
    
    def withdraw(self):
        while True:
            withdraw_amount = input("How much would you like to withdraw? Or type 'back' to go to the menu\n").lower().strip()
            
            try:
                value = float(withdraw_amount)
            
                if value <= 0:
                    print("Enter a valid number")
                
                elif value > self.balance:
                    print("You do not have that much. Please check your balance.\n")
                    break
                
                
                elif value > 0:
                    check = input (f"Are you sure you would like to withdraw ${value}?(yes/No)\n").lower().strip()
                    
                    if check == "yes":
                        self.balance -= value
                        print(f"Thank you for using bank name your new balance is {self.balance}")
                        break
            
            except ValueError:
                 withdraw_amount == "back"
                 break        



    def view_balance(self):
        while True:
            print(f"Your balance is ${self.balance}.")
            break

my_account = BankAccount()


print("Welcome to Pythopn Bank!")
def main():
    while True:
        print("1. View Balance")
        print("2. Withdraw")
        print("3. Deposit")1
        print("4. Quit")
        choice = input("What would you like to do today?\n").lower().strip()
        try:

            if choice == "1" or "view balance" in choice or "view" in choice:
                my_account.view_balance()
            
            elif choice == "2" or "withdraw" in choice:
                my_account.withdraw()
            
            elif choice == "3" or "deposit" in choice:
                my_account.deposit()
            
            elif choice == "4" or "quit" in choice:
                print("Thanks for using my Python Bank! Come Again!")
                break
            
        except ValueError:
            print("Invalid input try again.")
main()