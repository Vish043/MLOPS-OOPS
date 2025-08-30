#ingle or Basic Inheritance

#Basic class
# class Parent:
#     def __init__(self,name):
#         self.name = name
    
#     def greet (self):
#         print(f"Hello,my name is {self.name}.")

# class Child(Parent):
#     def plays(self):
#         print(f"{self.name} is playing.")

# child = Child("Alice")
# child.greet()
# child.plays()    

#***************************************************

# #Multilevel Inheritance
# #Base class
# class Grandparents:
#     def __init__(self,name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # Intermediate class
# class Parent(Grandparents):
#     def work(self):
#         print(f"{self.name} is working.")

# #Derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# child = Child("Charlie")
# child.tell_story()
# child.work()
# child.play()

#*****************************************************

#Hierarchical Inheritance

# class Parent:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()

#*********************************************

# #Multiple <Diamond Problem>
# # common class
# class A:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")
# #Intermediate Class 1
# class B(A):

#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()
# #Intermediate Class 2
# class C(A):

#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()
# #Derived Class
# class D(B,C):

#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# d = D("Frank")
# d.greet()

#**********************************************************

# Hybrid Inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

class mamal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Bat(mamal,Bird):
    def __init__(self,name):
        mamal.__init__(self,name)

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()