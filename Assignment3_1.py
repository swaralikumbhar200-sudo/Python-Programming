# write a program which accept N numbers from user and store it into list. Return Addition of all elements from that list.
# Input = no of elements= 6, Input elements= 13 5 45 7 4 56 output= 130

def Addition(Data):
        Sum = 0
        for No in Data:
                Sum = Sum + No

        return Sum



def main():
        n = int(input("Enter number of elements: "))

        list= []

        print("Enter the elements: ")

        for i in range(n):
                Value= int(input())
                list.append(Value)

        Ret = Addition(list)

        print("Addition of elements is: ", Ret)


if __name__ =="__main__":
        main()









