#Print a program which accepts one number and prints count of digit in that number.

n = int(input("enter a number:"))
count = 0

while n >0:
    
    n = n//10
    count +=1
    
print(count)

