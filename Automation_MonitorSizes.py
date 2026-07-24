#Write a Python program that monitors the size of a specified file every 30 seconds.
#Write the following details into: FileSizeLog.txt
#1.File path
#2.File size in bytes
#3.Date and time
#Handle the situation where the file does not exist.

import os
import time
import schedule
import datetime

def SizeofFile(Filepath):
   
    CurrentTime = datetime.datetime.now()
    

    if os.path.exists(Filepath):
        FileSize = os.path.getsize(Filepath)
    else:
        print("File does not exist")
        return

    fobj= open("FileSizeLog.txt", "a")
    fobj.write("File Path : " + Filepath + "\n")
    fobj.write("File size in bytes: "+ str(FileSize)+ "\n")
    fobj.write("Date and Time: "+ CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p ")+ "\n")
    fobj.write("-" * 40 + "\n")
    fobj.close()


def main():
    Filepath = input("Enter a file path: ")

    schedule.every(30).seconds.do(SizeofFile,Filepath)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()