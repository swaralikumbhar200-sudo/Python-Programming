#write a lambda function using reduce() which accepts a list of numbers and returns product of all elements.

from functools import reduce

ProductNum= lambda No1,No2 : No1 * No2

def main():
    Data = list(map(int, input("Enter numbers: ").split()))

    RData = reduce(ProductNum,Data)

    print("Data after reduce: ", RData)


if __name__ == "__main__":
    main()