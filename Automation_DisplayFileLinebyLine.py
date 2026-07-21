#Display File Line by Line
#Problem Statement:
#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
#Input:Demo.txt
#Expected Output:Display each line of Automation_Demo.txt one by one.

fobj = open("Automation_Demo.txt","r")
line = fobj.readline()       #first line
print(line)

line = fobj.readline()       #second line
print(line)

line = fobj.readline()       #Third line
print(line)

fobj.close()