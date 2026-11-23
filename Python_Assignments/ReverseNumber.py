#write a program which accepts one number and prints reverse of that number

n = int(input("Enter a number: "))
reverse = 0

while n>0:
    digit = n%10
    reverse = reverse*10 +digit
    n = n//10
print(reverse)