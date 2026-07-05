# write a lambda function using reduce() which accepts a list of numbers and returns addition of all elements.
from functools import reduce

Addition = lambda No1, No2: No1+No2

def main():
    Data = list(map(int, input("Enter number: "). split()))
    RData = reduce(Addition, Data)
    print("Data after Reduce: ",RData)

if __name__ =="__main__":
    main()