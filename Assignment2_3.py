# write a program which accept one number from user and returns its factorial. input = 5 and output = 120

n = int(input("Enter a number: "))
 
fact = 1
for i in range(1,n+1):
    fact *= i
print("Output is: ", fact)