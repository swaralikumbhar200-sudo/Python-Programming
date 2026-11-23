# write a program which accept N numbers from user and store it into list. Return minimum number from that list.
# Input = no of elements= 4, Input elements= 13 5 45 7  output= 5

def Minimum(Data):
    Min = Data[0]

    for No in Data:
        if No < Min:
            Min = No

    return Min

def main():

    n = int(input("Enter number of elements: "))

    list= []

    print("Enter the elements: ")

    for i in range(n):
        Value = int(input())
        list.append(Value)

    Ret = Minimum(list)
    print("Minimum number is : ", Ret)



if __name__ == "__main__":
    main()