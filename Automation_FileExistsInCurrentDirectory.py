#Check File Exists in Current Directory
#Problem Statement:
#Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
#Input:Automation_Demo.txt
#Expected Output:Display whether Automation_Demo.txt exists or not.

import os

Filename = input("Enter a File name: ")

if os.path.exists(Filename):
    print("File is present")
else:
    print("File is present")