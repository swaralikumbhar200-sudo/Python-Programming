# write a program which accept N numbers from user and store it into list. Accept one another number from user and return frequency of that number from list.
# Input = no of elements= 11, Input elements= 13 5 45 7 4 56 5 34 2 5 65 , element to search= 5,  output= 3


def Frequency(Data,Search):
    Count = 0
    for no in Data: 
        if no == Search:
            Count+= 1

    return Count




def main():
    n= int(input("Enter number of elements: "))

    list= []
    print("Enter the numbers: ")


    for i in range(n):
        Value = int(input())
        list.append(Value)

    Search = int(input("element to search: "))

    Ret = Frequency(list, Search)

    print("Frequency of number is: ", Ret)


if __name__ =="__main__":
    main()
