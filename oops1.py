#initiate a class
class Employee:
    # special method/magic method / dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "Software development Engineer"
        print("Attributes/data have been initiated")

    def travel(self,destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")

# create an obj/Instance of the class
sam = Employee()

# print sam id
#print(sam.salary)

# calling a method 
#sam.travel("Kerala")

print(type(sam))