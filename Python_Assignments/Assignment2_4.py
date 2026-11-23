# write a program which accept one number from user and return addition of its factors. input = 12, output = 16 (1+2+3+4+6)

n = int(input("Enter a number: "))

Sum= 0
i=1
while i< n:
    if n % i ==0:
       Sum= Sum + i
    i+=1
        
print("Addition is: ", Sum)
