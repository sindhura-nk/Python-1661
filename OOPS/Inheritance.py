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