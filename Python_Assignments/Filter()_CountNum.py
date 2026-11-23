#write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

CountEven = lambda No : No% 2 == 0

def main():
    Data = list(map(int, input("Enter numbers: ").split()))

    Count = len(list(filter(CountEven,Data)))

    print("Data after reduce: ", Count)

if __name__ =="__main__":
    main()