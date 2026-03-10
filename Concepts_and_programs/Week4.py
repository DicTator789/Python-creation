#Week 4 for OOPS And PEP8 code standards
#0 for custom exception
class MY_custom_exception(Exception):
    pass


#1
class Student:
    def __init__(self, name, marks, total):
        self.name = name
        self.marks = marks
        self.ALL_TOTAL = total
        # print("hello")

class Marks_info(Student):
    def display_marks(self):
        print(f"{self.name} got {self.marks}")

    def ispassed(self):
        percentage_of_marks = round(self.marks*100/self.ALL_TOTAL,2) 
        if(percentage_of_marks >= 33):
            print(f"{self.name} has passed and got {percentage_of_marks}%")
        else:
            print(f"{self.name} has failed the exam by {self.marks - self.ALL_TOTAL}")



# Student_1 = Marks_info("Rohit",654,700)

# Student_1.display_marks()
# Student_1.ispassed()



#2

class Bank_Account:

    def __init__(self, balance):
        self.current_balance = balance

    def deposit(self, deposit_amount):
        try:
            if(deposit_amount>0):
                self.current_balance += deposit_amount
                print(f"{deposit_amount} has been deposited to the bank")
            else:
                raise MY_custom_exception(f"{deposit_amount} should be valid amount")

        except:
            raise MY_custom_exception(f"{deposit_amount} is invalid : Please enter the proper amount to be deposited")

    def withdraw(self, withdraw_amount):
        try:
            if(withdraw_amount<=self.current_balance):
                self.current_balance-= withdraw_amount
                print(f"{withdraw_amount} has been withdrawed from the account")
            else:
                raise MY_custom_exception(f"{withdraw_amount} is greater than the {self.current_balance}")
        except:
            raise MY_custom_exception(f"{withdraw_amount} is invalid : Please enter the fair amount")
        
    def check_balance(self):
        print(f"the current balance is the account is {self.current_balance}")


Account_1 = Bank_Account(15000)

Account_1.check_balance()
Account_1.deposit(1220)
Account_1.check_balance()
Account_1.withdraw(15000)
Account_1.check_balance()