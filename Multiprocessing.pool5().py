#Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.
#Input :
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Task:
#For each number N, calculate: 2+4+6+8+......N
#Expected Output Format:
#Process ID : 1234
#Input Number : 1000000
#Sum of Even Numbers : 250000500000

from multiprocessing import Pool
import os

def SumEven(no):
    Sum = 0
    for num in range(2,no+1,2):
        Sum= Sum+num
    print("Process ID is: ", os.getpid())
    print("Input number is: ", no)
    print("Sum of even number is: ", Sum)

    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000]
    Result =[]
    pobj= Pool()
    Result= pobj.map(SumEven, Data)
    pobj.close()
    pobj.join()

    print("Result is: ")
    print(Result)

if __name__ == "__main__":
    main()
