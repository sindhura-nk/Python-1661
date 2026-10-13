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

        