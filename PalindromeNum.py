# write a program which accepts one number and checks whether it is palindrome or not? input =121 , output = Palindrome

n = int(input("Enter a number: "))
original =n
reverse = 0

while n>0:
    digit = n%10
    reverse = reverse*10+ digit
    n = n//10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
