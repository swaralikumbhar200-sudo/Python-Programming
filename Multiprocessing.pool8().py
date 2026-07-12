#Write a program that counts how many odd numbers exist between 1 and N using Pool.map().
#Input :
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Task:
#For each number N, calculate: 1,3,5,......N
#Expected Output Format:
#Process ID : 1237
#Input Number : 1000000
#Count of Odd Numbers : 500000

from multiprocessing import Pool
import os

def OddNum(no):
    Count = 0
    for i in range(1,no+1,2):
        Count= Count+1
    print("Process ID is: ", os.getpid())
    print("Input number is: ", no)
    print("Count of Odd number is: ", Count)

    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []
    pobj =Pool()
    Result = pobj.map(OddNum,Data)
    pobj.close()
    pobj.join()
    print("Result is: ")
    print(Result)

if __name__ =="__main__":
    main()

