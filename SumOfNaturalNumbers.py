# print a program which accepts one number and prints sum of first N natural nos

n= int(input("Enter a number"))

sum = 0
for i in range(1, n+1):
    sum += i

print(sum)