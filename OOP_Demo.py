#Write a Python program to implement a class named Demo with the following specifications:
#1.The class should contain two instance variables: no1 and no2.
#2. The class should contain one class variable named Value.
#3.Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
#4.Implement two instance methods:
#i) Fun() – displays the values of instance variables no1 and no2.
#ii)Gun() – displays the values of instance variables no1 and no2.
#Create two objects of the Demo class as follows:
#Obj1 = Demo(11, 21)

#Obj2 = Demo(51, 101)

#Call the instance methods in the given sequence:
#Obj1.Fun()
#Obj2.Fun()
#Obj1.Gun()
#Obj2.Gun()



class Demo:
    Value = 100

    def __init__(self,no1,no2):
        self.No1 = no1
        self.No2 = no2

    def Fun(self):
        print("Inside instance method Fun")
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print("Inside instance method Gun")
        print(self.No1)
        print(self.No2)



Obj1 = Demo(11,21)
Obj2 = Demo(51,101)


Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()