#print a program which accepts one number and prints multiplication table of that numbner

num = int(input("Enter a number"))

for i in range(1,11):
    print(i * num, end =" ")

