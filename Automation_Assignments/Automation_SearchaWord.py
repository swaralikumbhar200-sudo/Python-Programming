#Problem Statement:
#Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
#Input:Automation_Demo.txt  Marvellous
#Expected Output:Display whether the word Marvellous is found in Demo.txt or not.

fobj = open("Automation_Demo.txt", "r")
Data = fobj.read()
word = "Marvellous"

if word in Data:
    print("Word found in file")
else:
    print("Word not found in file")

fobj.close()