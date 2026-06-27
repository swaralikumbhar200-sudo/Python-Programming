def Divisible_by(num):
    if num % 3 == 0 and num % 5 ==0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

Num = int(input("Enter number",))
Divisible_by(Num)
