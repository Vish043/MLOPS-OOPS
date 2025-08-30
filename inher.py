# #Simple inheritance

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived class
# class Dog(Animal):

#     def speak(self):
#         print(f"{self.name}Buddy barks.")

# # # Create an Inheritance of Animal
# #animal = Animal("Generic Animal")
# #animal.speak() #Output: Generic Animal Makes a sound

# # # create an instance of Animal
# dog = Dog("buddy")
# dog.speak() # Output : Buddy barks.

#*********************************************
# super keyword ()

class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak1(self):
        #super().speak()
        print(f"{self.name} barks. It is a {self.breed}.")

dog = Dog("Golden Retriver")
dog.speak()