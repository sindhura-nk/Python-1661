# Single level inheritance
print("===Single level inheritance===")

'''
Scenario: Build a super class Employee that captures all the details of employee.
Build a child class Lead that inherits all the employee details and also has its own project details

Hierarchy:
Fresher -> Lead -> Manager -> Project Manager -> Delivery Head(Delivery Manager) -> Business Head
'''
# Parent class/super class
class Employee:
    # Class attributes
    Organization = "Tech Mahindra"
    Location = "Hinjewadi"

    # Instance attributes
    def __init__(self,name,emailID,emplocation):
        self.name = name
        self.emailID = emailID
        self.emplocation = emplocation

    # Display employee info
    def display_empdata(self):
        print(f"Employee details are: {self.name},employee email is {self.emailID}. Employee is lcoated at {self.emplocation}")

# Child class - Lead
class Lead(Employee):
    ## Instance attributes
    def __init__(self, name, emailID, emplocation,teamsize):
        super().__init__(name, emailID, emplocation)
        self.teamsize = teamsize

    # Display Lead information : Employee information + handling team size. 
    def lead_info(self):
        self.display_empdata()
        print(f"{self.name} is now promoted to Lead position and is handling a team of {self.teamsize} members.")

# Create instances of child class-Lead
emp_lead1 = Lead("Supriya","Supriya@gmail.com","Kharadi",5)
print("Access parent as well child attributes")
# Access parent as well child attributes
print(emp_lead1.name,emp_lead1.emailID,emp_lead1.emplocation,emp_lead1.teamsize)
print("-------------------")
# Access child methods
print("Access child methods")
emp_lead1.lead_info()


print("==========================================")
print("===================Hierarchal Inheritance=======================")
'''
Create a parent class Hyundai that has all car details, store details 
Create a child class economy that inherits Hyundai class as well as displays economy cars
Economy cars: Grand i10,Exter, Aura etc
Create a child class premium that inherits Hyundai class as well as displays premium cars
Premium cars: Creta Electric,IONIQ,Palisade etc
'''

class Hyundai:
    manager = "Raman" # class attribute

    @staticmethod
    def welcome():
        print("Welcome to Hyundai Showroom")
    def display_info(cls):
        print(F"Hello, I am {cls.manager}. We provide economy as well premium based cars. Share your budget and we will show you the right cars")

class economyHyundai(Hyundai):
    def __init__(self,max_pricerange):
        super().__init__()
        self.max_pricerange = max_pricerange

    def display_economy(self):
        # calling parent class methods
        self.welcome()
        self.display_info()
        # writing child class method code
        if self.max_pricerange>35:
            print(f"Explore our premium range.")
        else:
            print(f"We have Grand i10,Exter, Aura etc cars that fall under your required price range")

class premimumHyundai(Hyundai):
    def __init__(self,max_pricerange):
        super().__init__()
        self.max_pricerange = max_pricerange

    def display_premium(self):
        # calling parent class methods
        self.welcome()
        self.display_info()
        # writing child class method code
        if self.max_pricerange>35:
            print(f"We have Creta Electric,IONIQ,Palisade etc cars that fall under your required price range")
        else:
            print(f"THe minimum pricerange for premimum cars is 35 lakhs. Kindly explore our economy range that falls under your budget.")

# Create instances of child classes
print("Economy class")
cust1 = economyHyundai(23)
print(cust1.max_pricerange)
print(cust1.manager)
print("methods")
cust1.display_economy()

print("Premimum class")
cust2 = premimumHyundai(45)
print(cust2.manager)
print(cust2.max_pricerange)
print("methods")
cust2.display_premium()