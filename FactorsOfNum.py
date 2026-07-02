# write a program which accepts one number and print its factors. Input =12, output = 1 2 3 4 6 12

n = int(input("Enter a number: "))

for i in range(1,n+1):
    if n%i ==0:
        print(i,end =" ")
    

