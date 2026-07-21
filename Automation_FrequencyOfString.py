#Frequency of a String in File
#Problem Statement:
#Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) 
# of that string in the file.
#Input: Automation_Demo.txt  Marvellous
#Expected Output: Count how many times "Marvellous" appears in Demo.txt.

Filename = input("Enter a Filename: " )
Word = input("Enter a string to search: ")

fobj = open(Filename, "r")
Data = fobj.read()

Words = Data.split()

Count =0

for value in Words:
    if value == Word:
        Count = Count + 1

print("Frequency of", Word, "is:", Count)

fobj.close()