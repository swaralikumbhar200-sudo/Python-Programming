# write a lambda function using map() which accepts list of numbers and returns a list of squares of each number.

Square= lambda No : No * No

def main():
    Data = list(map(int, input("Enter nos:").split()))
    Mdata = list(map(Square,Data))
    print("Data after Map", Mdata)
   
if __name__ == "__main__":
    main()