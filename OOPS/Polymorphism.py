# Polymorphism - a method/operator taking multiple forms
# Method Overriding

# Operator Overriding
print("Operator Overriding")
print("Add 2 numbers : ", 45+56)
print("Concatenation","Raman"+" "+"Gaikwad")
print("Merge lists: ",[3,4,5]+[7,8,9])
print("product: ",2*3)
print("repetition of characters", "R"*3)
print("repetition of elements: ",[6]*5)

# Method overriding
print("Method overriding without Inheritance")

class India:
    def display_capital(self):
        print("Capital of India is Delhi")
class USA:
    def display_capital(self):
        print("Capital of USA is Washington")
'''
we can define a capital function which will take country instances(objects) as input
It retuns the capital of that country as output
'''
def capital(country_object):
    country_object.display_capital()

# create instances of India and USA classes
ind1 = India()
us1 = USA()

capital(ind1)
capital(us1)

# Method overriding  with Inheritance
class Vehicle:
    def display_vehicledetails(self):
        print(f"There are various types of vehicles: Electric,Petrol based, Diesel based and CNG based")
class Electric_Bike(Vehicle):
    def display_vehicledetails(self):
        print(f"Electric vehicles are environment friendly and also cost efficient")
print("============")
print("Method overriding with Inheritance")
# create instance of electric bike
elct = Electric_Bike()
elct.display_vehicledetails()
# create instance of parent vehicle
veh = Vehicle()
veh.display_vehicledetails()

