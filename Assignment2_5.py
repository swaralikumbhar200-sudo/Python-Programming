#write a program which accept one number from user and check whether number is prime or not. input = 5, output = It is prime number.

n= int(input("Enter a number: "))
Count = 0
for i in range(1,n+1):
    if (n%i == 0):
        Count +=1

if Count ==2:
        print("It is prime number")
else:
        print("It is not prime number")


