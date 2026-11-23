#write a program which contains filter(),map(),reduce() in it. Python application which contains one list of numbers. List contains
#the numbers which are accepted from the user. Filter should filter out all such nos which are Even.Map function will calculate its square.
#  Reduce will return the Addition of all that numbers.
#Input = [5,2,3,4,3,4,1,2,8,10]
#Data after filter = [2,4,4,2,8,10]
#Data after Map =[4,16,16,4,64,100]
#Data after Reduce = 204

from functools import reduce

CheckEven = lambda No : No%2 ==0
Square = lambda No : No* No
Addition = lambda No1,No2 : No1+ No2

def main():
    Data=list(map(int, input("Enter nos: ").split()))
    FData= list(filter(CheckEven,Data))
    print("Data after filter is: ", FData)

    MData= list(map(Square,FData))
    print("Data after Map is: ", MData)

    RData= reduce(Addition,MData)
    print("Data after Reduce is: ", RData)
    

if __name__ == "__main__":
        main()