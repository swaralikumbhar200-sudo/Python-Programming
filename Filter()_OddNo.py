# write a lambda function using filter() which accepts a list of numbers and returns list of odd number.

OddNumber = lambda No : No% 2 !=0

def main():
      
    Data = list(map(int, input("Enter number: ").split()))
    FData = list(filter(OddNumber,Data))
    print("Data after filter: ", FData)


if __name__ == "__main__":
    main()