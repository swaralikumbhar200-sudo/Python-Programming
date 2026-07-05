# write a lambda function using reduce () which accepts list of numbers and returns maximum element.

from functools import reduce
MaxNumber = lambda No1 ,No2 : No1 if No1>No2 else No2

def main():
    Data = list(map(int, input("Enter numbers: ").split()))
    RData = reduce(MaxNumber, Data)
    print("Maximum Element is: ", RData)

if __name__ == "__main__":
    main()