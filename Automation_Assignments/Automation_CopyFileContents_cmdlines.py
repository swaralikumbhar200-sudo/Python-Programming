#Copy File Contents into a New File (Command Line)
#Problem Statement:
#Write a program which accepts an existing file name through command line arguments, creates a new file named Automation_Demo1.txt, 
# and copies all contents from the given file into Automation_Demo1.txt.
#Input (Command Line):Automation_ABC1.txt
#Expected Output:Create Automation_Demo1.txt and copy contents of Automation_ABC1.txt into Automation_Demo1.txt.


import sys

Filename = sys.argv[1]

fobj1 = open(Filename,"r")
Data =fobj1.read()

fobj2 = open("Automation_Demo1.txt", "w")
fobj2.write(Data)

fobj1 .close()
fobj2.close()


