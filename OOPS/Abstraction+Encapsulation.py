'''
You hide the implementation details.
Inherit ABC class and also abstractmethod decorator.

Scenario: Create a Payment class where payment is done through UPI transaction. 
Hide these implementation details: Bank server connectivity, checking of the upi_id in the database
We will show only pay() to the user.

Encapsulation: combine data methods by providing different access levels:
1) protected : child classes can get the access of these protected methods/attributes
data or method as protected : you will _ infront of attribute name and method name
example: name = "Raman" public access
_name = "Raman protected access
2) private : Even child classes cannot get the access of private methods/attributes
data or method as private : you will __ infront of attribute name and method name
example: name = "Raman" public access
__name = "Raman private access
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
    def __init__(self,__upi_id,__password):
        super().__init__()
        self.__upi_id = __upi_id # private attribute
        self.__password = __password # private attribue
        self.connection = True
    # pay method-abstract method
    def pay(self):
        print("Intialising the payment process")
        self._check_upiID()
    # upi id valid or not
    def _check_upiID(self): # protected method
        if (self.__upi_id in data_upi_data.keys()) and (data_upi_data.get(self.__upi_id)==self.__password):
            self._bank_server_connectivity()
        else:
            print("Invalid UPI ID or Password. Retry again.")

    # bank server connectivity
    def _bank_server_connectivity(self): # protected method
        if self.connection:
            print("Server connection is successful. Amount is debited")
        else:
            print("connection unsuccessful. Contact branch")

    # private method
    def __display_upiID(self): # private method
        print(self.__upi_id)

# Creating child class for upi class
class gpay(upi):
    def __init__(self, __upi_id, __password):
        super().__init__(__upi_id, __password)
    def pay(self):
        print(f"{self.__password}") # child class is trying to access private attribute: error will be thrown
    def display(self):
        self._bank_server_connectivity() # child class is trying to access protected method: will be executed
        self.__display_upiID() # child class is trying to access private method: error will be thrown

# Create an instance of child class gpay
cust3_gpay = gpay("ewrwer","wererw")
cust3_gpay.display()
cust3_gpay.pay() # you must get an error : why? because private attributes and methods cannot be accessed by child classes
