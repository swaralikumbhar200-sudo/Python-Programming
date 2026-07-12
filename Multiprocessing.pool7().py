#Write a program that counts how many even numbers exist between 1 and N using Pool.map().
#Input :
#Data = [1000000, 2000000, 3000000, 4000000]
#Expected Task:
#For each number N, calculate: 2,4,6,......N
#Expected Output Format:
#Process ID : 1236
#Input Number : 1000000
#Count of Even Numbers : 500000

from multiprocessing import Pool
import os

def EvenNum(no):
    Count = 0
    for i in range(2,no+1,2):
        Count = Count+1
    print("Process ID is: ", os.getpid())
    print("Input number is: ", no)
    print("Count of Even number is: ", Count)

    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []
    pobj =Pool()
    Result = pobj.map(EvenNum,Data)
    pobj.close()
    pobj.join()
    print("Result is: ")
    print(Result)


if __name__ =="__main__":
    main()
