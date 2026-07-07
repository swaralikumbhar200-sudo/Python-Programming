#Create on module named as Arithmetic which contains 4 functions as Add() for Addition, Sub()for subtraction, Mult()for multiplication and Div() for Division.
#All functions accepts two parameters as number and perform the operation. Write on python program which call all the function from Arithmetic module by accepting the parameters from user.

import ArithmeticModule

def main():
    Value1 = int(input("Enter first number: "))

    Value2 = int(input("Enter second number: "))

    Ret = ArithmeticModule.Add(Value1,Value2)

    print("Addition is: ", Ret)

    Ret = ArithmeticModule.Sub(Value1,Value2)

    print("Subtraction is: ", Ret)

    Ret = ArithmeticModule.Mult(Value1,Value2)

    print("Multiplication is: ", Ret)

    Ret = ArithmeticModule.Div(Value1,Value2)

    print("Division is: ", Ret)

if __name__ =="__main__":
    main()
