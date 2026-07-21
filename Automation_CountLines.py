#Count Lines in a File
#Problem Statement: Write a program which accepts a file name from the user and counts how many lines are present in the file.
#Input:  Demo.txt
#Expected Output: Total number of lines in Automation_Demo.txt.

fobj = open("Automation_Demo.txt" , "r")

Count = 0

for line in fobj:
    Count = Count+1
    
print("Total number of Lines: ", Count)

    
fobj.close()