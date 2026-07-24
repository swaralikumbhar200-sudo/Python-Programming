#Write a program that creates a new text file every minute.
#The filename should contain the current timestamp.
#Example: File_25_07_2026_16_30_00.txt
#Write the following information into the file:
#1.Filename
#2.Creation date
#3.Creation time

import datetime
import schedule
import time

def Logfile():

    CurrentTime = datetime.datetime.now()

    Date = CurrentTime.strftime("%d-%m-%Y")
    Time = CurrentTime.strftime("%H:%M:%S")

    Filename = "File_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S")+ ".txt"

    fobj = open(Filename,"w")
    fobj.write("Filename: "+ Filename + "\n")
    fobj.write("Creation Date: "+ Date + "\n")
    fobj.write("Creation Time: "+ Time + "\n")
    fobj.close()


def main():
    schedule.every().minute.do(Logfile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
