#Display File Contents
#Problem Statement:
#Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
#Input: Automation_Demo.txt
#Expected Output:Display contents of Demo.txt on console.

Filename = input("Enter a File name: ")
fobj = open(Filename, "r")
for line in fobj:
    print(line)

fobj.close()
