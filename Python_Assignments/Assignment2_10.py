# write a program which accept number from user and return addition of digits of that number. input = 5187934 , output = 37

n = int(input("Enter a number: "))
Sum = 0
while n>0:
    last_digit = n % 10
    Sum = Sum+ last_digit
    n= n//10

print(Sum)
