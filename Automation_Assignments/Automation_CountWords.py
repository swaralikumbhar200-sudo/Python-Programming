#Count Words in a File
#Problem Statement: Write a program which accepts a file name from the user and counts the total number of words in that file.
#Input:  Demo.txt
#Expected Output: Total number of words in Automation_Demo.txt

fobj = open("Automation_Demo.txt", "r")
count = 0
for line in fobj:
    words = line.split()
    count= count+len(words)

print("Total number of words: ",count)

fobj.close()
