#Copy File Contents into Another File
#Problem Statement:
#Write a program which accepts two file names from the user.
#First file is an existing file.
#Second file is the new file to be created.
#Copy all the contents from the first file into the second file.
#Input:Automation_Demo.txt  Automation_ABC.txt
#Expected Output:Contents of Automation_Demo.txt copied into Automation_ABC.txt

fobj1 =open("Automation_Demo.txt", "r")
Data = fobj1.read()

fobj2 = open("Automation_ABC.txt", "w")
fobj2.write(Data)

print("File copied Successfully")

fobj1.close()
fobj2.close()
