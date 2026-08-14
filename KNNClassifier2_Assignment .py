#Write a Python program that demonstrates how prediction changes when K changes.
#Predict the class of the same new point using:
#1.K = 1
#2.K = 3
#3.K = 5
import math

def EUCDistance(P1,P2):
    Ans = math.sqrt((P1['X']- P2['X'])**2 + (P1['Y']- P2['Y'])**2)
    return Ans


def KNNClassifier():
    border = "-"*30
    print(border)

    Data = [
        {'Point': 'A', 'X' : 1 ,'Y' : 2, 'Label': 'Red'},
        {'Point': 'B', 'X' : 2 ,'Y' : 3, 'Label': 'Red'},
        {'Point': 'C', 'X' : 3 ,'Y' : 1, 'Label': 'Blue'},
        {'Point': 'D', 'X' : 6 ,'Y' : 5, 'Label': 'Blue'},
        {'Point': 'E', 'X': 5, 'Y': 2, 'Label': 'Blue'}
    ]

    print("Training Data is: ")
    for i in Data:
        print(i)

    print(border)

    #Step1: new_point
    new_X = float(input("Enter 'X' cordinate: "))
    new_Y = float(input("Enter 'Y' cordinate: "))
    new_point ={
        'X' : new_X,
        'Y' : new_Y
    }

   #Step 2: Calculate Distances:
    for d in Data:
        d['distance'] = EUCDistance(d,new_point)
    print("Calculated Distances: ")

    for d in Data:
        print(d)

    print(border)

    #Step 3: Sort the distances:
    Sorted_Data = sorted(Data,key=lambda item:item['distance'])

    print("Sorted data is: ")

    for d in Sorted_Data:
        print(d)

    print(border)

    #Step 4: Condition1- select k =1 nearest neighbors:
    K =1
    K_nearest = Sorted_Data[:K]
    print("Nearest Neighbors_1: ")

    for d in K_nearest:
        print(d)

    #Step 5: Prediction:

    red = sum(1 for i in K_nearest if i['Label']=="Red")
    blue = sum(1 for i in K_nearest if i['Label']=="Blue")

    print(f"Red Votes = {red}, Blue Votes = {blue}")

    if red>blue:
        print("Prediction is : Red")
    else:
        print("Prediction is : Blue")

    print(border)

    #Step 4: Condition3- select k =1 nearest neighbors:
    K =3
    K_nearest = Sorted_Data[:K]
    print("Nearest Neighbors_3: ")

    for d in K_nearest:
        print(d)

    #Step 5: Prediction:

    red = sum(1 for i in K_nearest if i['Label']=="Red")
    blue = sum(1 for i in K_nearest if i['Label']=="Blue")

    print(f"Red Votes = {red}, Blue Votes = {blue}")

    if red>blue:
        print("Prediction is : Red")
    else:
        print("Prediction is : Blue")

    print(border)

    #Step 4: Condition3- select k =5 nearest neighbors:
    K =5
    K_nearest = Sorted_Data[:K]
    print("Nearest Neighbors_5: ")

    for d in K_nearest:
        print(d)

    #Step 5: Prediction:

    red = sum(1 for i in K_nearest if i['Label']=="Red")
    blue = sum(1 for i in K_nearest if i['Label']=="Blue")

    print(f"Red Votes = {red}, Blue Votes = {blue}")

    if red>blue:
        print("Prediction is : Red")
    else:
        print("Prediction is : Blue")

def main():
    KNNClassifier()

if __name__ =="__main__":
    main()

#The prediction can change when K increases because K decides how many nearest neighbors participate in the voting.