name = "Raman"
print(type(name))

print("============CLASS=============")

class ThreeRI:
    #Instance Attributes 
    def __init__(self,name,emailID,profession):
        self.name = name
        self.emailID = emailID
        self.profession = profession

    # methods - functions inside a class
    def display(self):
        return f"Welcome to 3RI. Your details are: {self.name},{self.emailID} and {self.profession}. Can you confirm your details?"

# Create an instance of class ThreeRI
student1 = ThreeRI("Raman","Raman@gmail.com","Student")
student2 = ThreeRI("Suman","Suman@gmail.com","Sales Manager")

# Accessing attributes
print("========Accessing Attributes=========")
print("student1",student1.name,student1.emailID,student1.profession)
print("student2",student2.name,student2.emailID,student2.profession)

print("========Accessing Methods=========")
display_student1 = student1.display()
print("student1",display_student1)

display_student2 = student2.display()
print("student2",display_student2)

print("=================class attributes and instance attributes====================")
class Bank:
    # class attributes
    Branch_Manager = "Thaman Shinde"
    Location = "Pimple Saudagar"

    # Init constructor
    def __init__(self,acc_number,name,balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance
        self.userkey = "34USER"

    # Display balance
    def show_balance(self):
        return f"Your balance is {self.balance}"

    # Withdraw amount    
    def withdrawal(self,amount):
        self.amount = amount
        if self.amount < self.balance:
            self.balance -= self.amount
            print(f"{self.amount} Amount withdrawn successfully. Updated Balance is {self.balance}")
        else:
            print("Insufficient Balance")

    # Class attributes
    def welcome(cls):
        print(f"Hello User. Welcome to our branch located at {cls.Location}. I am {cls.Branch_Manager}, Branch Manager. COntact me in case of complaints or suggestions")

    # MEthods can be defined without considering self attribute as input
    @staticmethod # decorator
    def greet():
        print("Welcome to our branch. Visit ur again")

# Create an instance of Bank class
customer1 = Bank(3454356546,"Priya",67000)
customer2 = Bank(23423432,"Riya",3000)

# Access class attributes
print("============Class attributes==========")
print("customer1",customer1.Branch_Manager,customer1.Location)
print("customer2",customer2.Branch_Manager,customer2.Location)

# Access Instance attributes
print("==========Instance attribute==============")
print("customer1",customer1.name,customer1.acc_number,customer1.balance,customer1.userkey)
print("customer2",customer2.name,customer2.acc_number,customer2.balance,customer2.userkey)

## Access methods
print("======methods========")
print("Welcome")
customer1.welcome()

print("show balance")
bal = customer1.show_balance()
print(bal)
# print(customer1.show_balance())

print("withdrawal process")
customer1.withdrawal(90000)
customer1.withdrawal(3400)

print("staticmethod")
customer1.greet()
        