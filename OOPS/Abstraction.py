'''
You hide the implementation details.
Inherit ABC class and also abstractmethod decorator.

Scenario: Create a Payment class where payment is done through UPI transaction. 
Hide these implementation details: Bank server connectivity, checking of the upi_id in the database
We will show only pay() to the user.
'''
from abc import ABC,abstractmethod
# Creating user data dictionary
data_upi_data = {"RA@34534HDFC.in":"RAM@N3234","TH@676567ICIC.in":"T#@45mn"}
class Bank(ABC):
    @abstractmethod
    def pay(self):
        pass

class upi(Bank):
    # Instance attributes
    def __init__(self,upi_id,password):
        super().__init__()
        self.upi_id = upi_id
        self.password = password
        self.connection = True
    # pay method-abstract method
    def pay(self):
        print("Intialising the payment process")
        self.check_upiID()
    # upi id valid or not
    def check_upiID(self):
        if (self.upi_id in data_upi_data.keys()) and (data_upi_data.get(self.upi_id)==self.password):
            self.bank_server_connectivity()
        else:
            print("Invalid UPI ID or Password. Retry again.")

    # bank server connectivity
    def bank_server_connectivity(self):
        if self.connection:
            print("Server connection is successful. Amount is debited")
        else:
            print("connection unsuccessful. Contact branch")

# Instance of the class
print("=====correct upid==========")
cust1 = upi("RA@34534HDFC.in","RAM@N3234")
cust1.pay()

print("========wrong password=========")
cust2 = upi("RA@34534HDFC.in","sdsfsdf")
cust2.pay()