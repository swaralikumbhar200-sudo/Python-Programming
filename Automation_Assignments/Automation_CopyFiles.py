#Write a program that copies all .txt files from one directory to another every ten minutes.
#The program should:
#1.Accept source and destination directories.
#2.Validate both directories.
#3.Copy only .txt files.
#4.Maintain a log of copied files.
#5.Avoid terminating if one file cannot be copied.


import os
import shutil
import time
import schedule
import datetime

def CopyTxtFiles(Source, Destination):

    if not os.path.isdir(Source):
        print("Source directory does not exist")
        return

    if not os.path.isdir(Destination):
        print("Destination directory does not exist")
        return

    LogFile = open("CopyLog.txt", "a")

    for File in os.listdir(Source):

        SourcePath = os.path.join(Source, File)

        if os.path.isfile(SourcePath) and File.endswith(".txt"):

            try:
                shutil.copy(SourcePath, Destination)

                CurrentTime = datetime.datetime.now()

                LogFile.write("Copied File : " + File + "\n")
                LogFile.write("Date and Time : " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                LogFile.write("-" * 40 + "\n")

                print(File, "copied successfully")

            except Exception:
                print(File, "cannot be copied")

    LogFile.close()


def main():

    Source = input("Enter source directory: ")
    Destination = input("Enter destination directory: ")

    schedule.every(10).minutes.do(CopyTxtFiles, Source, Destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()