#write a lambda function using reduce () which accepts list of numbers and returns minimum element.

from functools import reduce

MinNumber = lambda No1, No2 : No1 if No1<No2 else No2

def main():
    Data = list(map(int, input("Enter Numbers: ").split()))
    RData = reduce(MinNumber,Data)
    print("Minimum Number is: ", RData)

if __name__ == "__main__":
    main()