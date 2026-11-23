#Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.
#Input :
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Task:
#For each number N, calculate: 1+3+5+......N
#Expected Output Format:
#Process ID : 1235
#Input Number : 1000000
#Sum of Even Numbers : 250000000000

from multiprocessing import Pool
import os

def SumOdd(no):
    Sum = 0
    for i in range(1,no+1,2):
        Sum= Sum+i
    print("Process ID is: ", os.getpid())
    print("Input number is: ", no)
    print("Sum of odd number is: ", Sum)
    return Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    Result=[]
    pobj = Pool()
    Result = pobj.map(SumOdd,Data)
    pobj.close()
    pobj.join()
    print("Result is: ")
    print(Result)

if __name__ =="__main__":
    main()