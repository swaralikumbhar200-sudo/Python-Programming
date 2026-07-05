# write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by 3 and 5.

Check_Divisible = lambda No :(No%3 ==0) and (No%5==0)

def main():
    Data = list(map(int, input("Enter numbers: ").split()))

    FData = list(filter(Check_Divisible, Data))

    print(" Data after filter: ",FData)

if __name__ == "__main__":
    main()