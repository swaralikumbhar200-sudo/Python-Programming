# write a program which accepts one number and checks whether it is perfect number or not? input = 6, output = perfect number.

n = int(input("Enter a number: "))
sum = 0
 

for i in range(1,n):
     if n % i ==0:
        sum += i

if sum==n:
        print("Perfect Number")
else:
        print("Not Perfect Number")


    
