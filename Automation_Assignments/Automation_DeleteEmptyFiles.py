#Write a program that deletes all empty files from a specified directory every hour.
#The program should:
#1.Scan the directory recursively.
#2.Detect files whose size is zero bytes.
#3.Delete the empty files.
#4.Store deleted file paths in a log file.
#5.Handle permission errors.
# Note: Test the program only on a sample directory.


import os
import time
import schedule
import datetime

def DeleteEmptyFiles(DirName):

    if not os.path.isdir(DirName):
        print("Directory does not exist")
        return

    LogFile = open("DeleteLog.txt", "a")

    for FolderName, SubFolder, FileNames in os.walk(DirName):

        for File in FileNames:

            FilePath = os.path.join(FolderName, File)

            try:

                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    CurrentTime = datetime.datetime.now()

                    LogFile.write("Deleted File : " + FilePath + "\n")
                    LogFile.write("Date and Time : " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                    LogFile.write("-" * 40 + "\n")

                    print(FilePath, "deleted")

            except PermissionError:
                print("Permission denied :", FilePath)

    LogFile.close()


def main():

    DirName = input("Enter directory path: ")

    schedule.every(1).hours.do(DeleteEmptyFiles, DirName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()