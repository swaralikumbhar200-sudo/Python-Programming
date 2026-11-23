# write a program which accept N numbers from user and store it into list. Return maximum number from that list.
# Input = no of elements= 7, Input elements= 13 5 45 7 4 56 34 output= 56

def Maximum(Data):
    Max = Data[0]

    for No in Data:
        if No>Max:
            Max = No

    return Max
    

def main():

    n = int(input("Enter number of elements: "))

    list= []

    print("Enter the elements: ")

    for i in range(n):
        Value = int(input())
        list.append(Value)

    Ret = Maximum(list)
    print("Maximum number is : ", Ret)


if __name__ =="__main__":
    main()