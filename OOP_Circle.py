#Write a Python program to implement a class named Circle with the following requirements:
#The class should contain three instance variables:
#1.Radius
#2.Area
#3.Circumference
#The class should contain one class variable named PI, initialized to 3.14.
#Define a constructor (__init__) that initializes all instance variables to 0.0.
#Implement the following instance methods:
#1)Accept()
#Accepts the radius of the circle from the user.
#2)CalculateArea()
#Calculates the area of the circle and stores it in the Area variable.
#3)CalculateCircumference()
#Calculates the circumference of the circle and stores it in the Circumference variable.
#4)Display()
#Displays the values of Radius, Area, and Circumference.
#Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self . Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self. Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius: ", self.Radius)
        print("Area: ", self.Area)
        print("Cicumference: ", self.Circumference)


obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2 = Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()







