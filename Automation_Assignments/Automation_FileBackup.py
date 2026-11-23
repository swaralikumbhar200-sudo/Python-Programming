#Write a Python program that performs a file backup every hour.
#The program should:
#1.Accept the source file path.
#2.Accept the destination directory path.
#3.Copy the source file to the destination directory.
#4.Add the current date and time to the backup filename.
#5.Write the backup operation details into:
#backup_log.txt: Example backup filename:
#Data_25_07_2026_16_30_00.txt: Example log entry
#Backup completed successfully at 25-07-2026 04:30:00 PM
#Use the shutil module for file copying.


import datetime
import os
import schedule
import time
import shutil

def Backup():
    Source = input("Enter source file path name: ")

    Destination = input("Enter the destination directory path: ")

    CurrentTime = datetime.datetime.now()

    Filename = os.path.basename(Source)

    Name, Extension = os.path.splitext(Filename)

    BackupFile = Name + "_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S")+ Extension

    DestinationPath = os.path.join(Destination,BackupFile)

    shutil.copy(Source,DestinationPath)

    fobj= open("backup_log.txt","a")

    fobj.write("Backup completed successfully at "+ CurrentTime.strftime("%d_%m_%Y %I:%M:%S %p")+ "\n")

    fobj.close()

def main():
    schedule.every(1).hour.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()