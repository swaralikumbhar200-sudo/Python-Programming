# print a program which accepts one number and prints factorial of that number.

n = int(input("Enter a number:"))

fact = 1
for i in range(1,n+1):
    fact *= i

print("Output is:" ,fact)