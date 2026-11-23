#write a program which contains filter(),map(),reduce() in it. Python application which contains one list of numbers. List contains
#the numbers which are accepted from the user. Filter should filter out all prime numbers .Map function will multiply each number by 2.
#  Reduce will return the maximum number from that numbers.
#Input = [2,70,11,10,17,23,31,77]
#Data after filter = [2,11,17,23,31]
#Data after Map =[4,22,34,46,62]
#Data after Reduce = 62

from functools import reduce

CheckPrime = lambda No : No>1 and all(No % i != 0 for i in range(2, No))
Multiply = lambda No : No*2
Maximum = lambda No1,No2 : No1 if  No1> No2 else No2

def main():
    Data=list(map(int, input("Enter nos: ").split()))
    FData= list(filter(CheckPrime,Data))
    print("Data after filter is: ", FData)

    MData= list(map(Multiply,FData))
    print("Data after Map is: ", MData)

    RData= reduce(Maximum,MData)
    print("Data after Reduce is: ", RData)
    

if __name__ == "__main__":
        main()