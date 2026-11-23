# write a program which accepts two numbers and prints Addition,subtraction,Multiplicatin,Division.
No1= int(input("Enter a first number:"))
No2 =int(input("Enter a second number:"))

Addition = No1+ No2
Subtraction = No1- No2
Multiplication = No1 *No2
Division= No1 / No2

def main():
    print("Addition is:", Addition)

    print("Subtraction is:", Subtraction)

    print("Multiplication is:", Multiplication)

    print("Division is:", Division)

if __name__ == "__main__":
    main()



