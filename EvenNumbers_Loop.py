#print a program which accepts one number and prints all even numbers till that number. input = 10, output = 2 4 6 8 10

n = int(input("Enter a number:"))

for i in range(2,n+1,2):
    print(i, end = " ")
