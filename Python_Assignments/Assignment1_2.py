# write a program which contains one function named as ChkNum() which accept one parameter as a number. if the number is even then it should display "Even no". otherwise display "Odd no."

n= int(input("Enter a number: "))

def ChkNum():
    if (n % 2==0):
        print("Even number")
    else:
        print("Odd number")

ChkNum()