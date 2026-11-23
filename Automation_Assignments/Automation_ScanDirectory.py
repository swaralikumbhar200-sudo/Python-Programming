#Write a program that scans a specified directory every minute.
#The task should display:
#1.Directory name
#2.Number of files
#3.Number of subdirectories
#4.Date and time of scanning
#Use the os module.
#Example output:
#Directory Scanned: E:/Data
#Total Files: 15
#Total Subdirectories: 4
#Scan Time: 25-07-2026 04:30:00 PM

import os
import datetime
import schedule
import time

def ScanDirectory():
    Directory = input("Enter Directory Path: ")
    Files = 0
    Subdirectories = 0

    for Name in os.listdir(Directory):
        Path = os.path.join(Directory,Name)

        if os.path.isfile(Path):
            print("File: ", Name)
            Files = Files+1

        elif os.path.isdir(Directory):
            print("Folder: ", Name)
            Subdirectories = Subdirectories+1

    print("Directory Scanned : ", Directory)
    print("Total Files: ",Files)
    print("Total Subdirectories: ",Subdirectories)
    print("Scan Time: ",datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-------------------------------------------------------------------")
        
def main():
    schedule.every(1).minute.do(ScanDirectory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()


