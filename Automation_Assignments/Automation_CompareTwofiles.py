#Compare Two Files (Command Line)
#Problem Statement:
#Write a program which accepts two file names through command line arguments and compares the contents of both files.
#1.If both files contain the same contents, display Success.
#2.Otherwise display Failure.
#Input (Command Line):Automation_Demo.txt  Automation_ABC.txt
#Expected Output: Success OR Failure

import sys

Filename1 = sys.argv[1]
fobj1 = open(Filename1,"r")
Data1 =fobj1.read()

Filename2 = sys.argv[2]
fobj2 = open(Filename2,"r")
Data2 = fobj2.read()

if Data1 == Data2:
    print("Success")
else:
    print("Failure")

fobj1.close()
fobj2.close()