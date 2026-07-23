#Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.
#Write the result into:
#DirectoryCountLog.txt
#Each entry should contain:
#1.Directory path
#2.Number of files
#3.Date and time

import os
import time
import datetime
import schedule

def CountFiles(Directory):
    CurrentTime= datetime.datetime.now()

    
    Files = 0

    for name in os.listdir(Directory):
        Path = os.path.join(Directory, name)

        if os.path.isfile(Path):
            Files = Files + 1

    fobj =open("DirectoryCountLog.txt" , "a")
    fobj.write("Directory Path: "+ Directory +"\n")
    fobj.write("Number of files: "+str(Files) +"\n")
    fobj.write("Date and Time: " +CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write("-------------------------------------------------------------\n")

    fobj.close()


def main():
    Directory= input("Enter a directory Path: ")

    schedule.every(5).minutes.do(CountFiles,Directory)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()
