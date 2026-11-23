#Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
#Input = [10, 15, 20, 25]
# Display:
#Process ID
#Input Number
#Factorial



from multiprocessing import Pool
import os

def Factorial(no):
    
    Factorial= 1
    for i in range(1,no+1):
        Factorial*= i

    print("Total number of cpu cores: ", os.cpu_count())
    print("Process ID : ", os.getpid())
    print("Input Number : ", no)
    print("Factorial : ", Factorial)
    print("------------------------")

    return Factorial

def main():
    n= int(input("Enter the number of elements: "))
    Data=[]
    for i in range(n):
        Value = int(input())
        Data.append(Value)

    Result=[]
    pobj=Pool()
    Result= pobj.map(Factorial,Data)
    pobj.close()
    pobj.join()

    print("Result is: ")
    print(Result)


if __name__ =="__main__":
    main()
