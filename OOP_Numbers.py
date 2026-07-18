#Write a Python program to implement a class named Numbers with the following specifications:
#1.The class should contain one instance variable:
#i)Value
#Define a constructor (__init__) that accepts a number from the user and initializes Value.
#Implement the following instance methods:
#1.ChkPrime() – returns True if the number is prime, otherwise returns False.
#2.ChkPerfect() – returns True if the number is perfect, otherwise returns False.
#3.Factors() – displays all factors of the number.
#4.SumFactors() – returns the sum of all factors.
#Create multiple objects and call all methods.


class Numbers:
    pass

    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        Count = 0

        for i in range(1,self.Value+1):
            if self.Value % i ==0:
                Count = Count+1
        

        if Count == 2:
            return True
        else:
            return False
        

    def ChkPerfect(self):
        Sum = 0

        for i in range(1,self.Value):
            if self.Value%i ==0:
                Sum = Sum + i

        if Sum == self.Value:
                return True
        else:
                return False
            
    def Factors(self):
        print("Factors are: ")
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value+1):
            if self.Value % i ==0 :
                Sum = Sum + i

        return Sum
    

obj1 = Numbers(28)
print("Prime: " ,obj1.ChkPrime())
print("Perfect: ", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors: ", obj1.SumFactors())

       

