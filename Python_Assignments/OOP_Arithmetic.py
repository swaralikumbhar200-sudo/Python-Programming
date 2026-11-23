#Write a Python program to implement a class named Arithmetic with the following characteristics:
#1.The class should contain two instance variables:
 #i)Value1
 #ii)Value2
#2.Define a constructor (__init__) that initializes all instance variables to 0.
#3.Implement the following instance methods:
  #i)Accept()
#Accepts values for Value1 and Value2 from the user.
  #ii)Addition()
#Returns the addition of Value1 and Value2.
  #iii)Subtraction()
#Returns the subtraction of Value1 and Value2.
  #iv)Multiplication()
#Returns the multiplication of Value1 and Value2.
  #v)Division()
#Returns the division of Value1 and Value2 (handle division by zero properly).
#Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    pass

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter a Value1: "))
        self.Value2 = int(input("Enter a Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return ("Division by zero is not possible")
        return self.Value1 / self.Value2
    


obj1 = Arithmetic()
obj1.Accept()
print("Addition: ",obj1.Addition())
print("Subtraction: ",obj1.Subtraction())
print("Multiplication : ",obj1.Multiplication())
print("Division : ",obj1. Division())
    

obj2 = Arithmetic()
obj2.Accept()
print("Addition: ",obj2.Addition())
print("Subtraction: ",obj2.Subtraction())
print("Multiplication : ",obj2.Multiplication())
print("Division : ",obj2. Division())
    
