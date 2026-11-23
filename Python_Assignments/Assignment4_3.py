#write a program which contains filter(),map(),reduce() in it. Python application which contains one list of numbers. List contains
#the numbers which are accepted from the user. Filter should filter out all such nos which greater than or equal to 70 and less than 
# or equal to 90.Map should increase each number by 10. Reduce will return the product of all that numbers.
#Input = [4,34,36,76,68,24,89,23,86,90,45,70]
#Data after filter = [76,89,86,90,70]
#Data after Map =[86,99,96,100,80]
#Data after Reduce = 6538752000

from functools import reduce

CheckNumber = lambda No : 70<= No<=90
Increment = lambda No : No+10
Multiplication = lambda No1,No2 : No1* No2

def main():
    Data=list(map(int, input("Enter nos: ").split()))
    FData= list(filter(CheckNumber,Data))
    print("Data after filter is: ", FData)

    MData= list(map(Increment,FData))
    print("Data after Map is: ", MData)

    RData= reduce(Multiplication,MData)
    print("Data after Reduce is: ", RData)
    

if __name__ == "__main__":
        main()