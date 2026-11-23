#Write a program that creates a new log file after every ten minutes.
#The filename should contain the current date and time.
#Example:
#MarvellousLog_25_07_2026_16_30_00.txt
#The file should contain:
#1.Log file created successfully.
#2.Creation Time: 25-07-2026 04:30:00 PM


import datetime
import schedule
import time


def LogFile():
    CurrentTime = datetime.datetime.now()

    
    LogFilename= "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(LogFilename, "w")
    fobj.write("Log file created successfully. \n" )
    fobj.write("Creation Time: "+ CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.close()


def main():
    schedule.every(10).minutes.do(LogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ =="__main__":
    main()