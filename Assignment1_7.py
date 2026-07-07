# write a program which contains one function that accept one number from user and returns true if number is divisible by 5 , otherwise return false.
#input = 8  output = false , input = 25  output = True.

n= int(input("Enter a number: "))

def main():
    if(n % 5 == 0):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()