# write a program which accept number from user and return number of digits of that number. input = 5187934 , output = 7

n = int(input("Enter a number: "))

count=0

while n>0:
     n = n//10
     count+=1
   

print(count)