#Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
#Input :
#Data = [10,15,20,25]
#Expected Task:
#For each number N, calculate: N!
#Expected Output Format:
#Process ID : 1240
#Input Number : 20
#Factorial: 2432902008176640000

from multiprocessing import Pool
import os

def Factorial(no):
    Factorial=1
    for i in range(1,no+1):
        Factorial = Factorial *i

    print("Process ID is: ", os.getpid())
    print("Input number is: ", no)
    print("Factorial is: ", Factorial)

    return Factorial

def main():
    Data = [10,15,20,25]
    Result = []
    pobj = Pool()
    Result = pobj.map(Factorial,Data)
    pobj.close()
    pobj.join()
    print("Result is: ")
    print(Result)

if __name__ =="__main__":
    main()
