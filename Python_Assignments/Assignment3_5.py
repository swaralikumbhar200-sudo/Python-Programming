#write a program which accept N nos from user and store it into list. Return Addition of all prime nos from that list. Main python file accepts N numbers from user and pass each number to CheckPrime()function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime(). 
#input = no of elements= 11 , Input elements= 13 5 45 7 4 56 10 34 2 5 8 , Output = 32(13+5+7+5+2).
import MarvellousNumModule

def ListPrime(Data):
    Sum=0
    for No in Data:
        if MarvellousNumModule.CheckPrime(No):
            Sum = Sum+ No

    return Sum


def main():
    n = int(input("Enter no of elements: "))

    list=[]

    print("Enter the elements:")

    for i in range(n):
        Value = int(input())
        list.append(Value)

    Ret = ListPrime(list)

    print("Addition Of Prime number is: ", Ret)

if __name__ == "__main__":
    main()


    