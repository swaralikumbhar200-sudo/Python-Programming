print("-----------------------------------------------------------------------------------------------------------")
print("----------------------------------------------Ticket House-------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------")

name = input("Enter your name : ")
age = int(input("Enter your age : "))

if(age>0 and age<=5):
    print(name, "you are having free entry")

elif(age>5 and age<=18):
    print(name,"your entry ticket is 900")

elif(age>18 and age<=40):
    print(name,"your entry ticket is 1200")

else:
    print(name,"you are not allowed")