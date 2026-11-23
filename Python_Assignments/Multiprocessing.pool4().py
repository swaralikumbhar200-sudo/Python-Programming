#Write a program that calculates , 1^5+2^5+3^5+....+N^5 for multiple values of N simultaneously using Pool.
#Input = [1000000,
#2000000,
#3000000,
#4000000]
#Display:
#    1)Measure total execution time.

import time
from multiprocessing import Pool

def Calculation(no):
    Total = 0
    for num in range(1,no+1):
        Total= Total+ (num**5)
    
    return Total

def main():
    Data =[1000000,2000000,3000000,4000000]

    start_time = time.perf_counter()
    Result=[]
    pobj=Pool()
    Result = pobj.map(Calculation,Data)
    pobj.close()
    pobj.join()

    end_time= time.perf_counter()

    print("Result:")
    print(Result)

    print(f"Total Execution Time :{end_time-start_time: .4f}seconds")
    

if __name__ == "__main__":
    main()
