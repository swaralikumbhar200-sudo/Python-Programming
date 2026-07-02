#write a program which accepts one number and prints that many numbers in reverse order. input = 5 , output = 5 4 3 2 1

n= int(input("Enter a number:" ))

for i in range(n,0,-1):
    print(i, end = " ")