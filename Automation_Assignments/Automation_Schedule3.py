#Write a program that schedules the following messages:
#1.Monday at 9:00 AM: Start your weekly goals
#2.Wednesday at 5:00 PM: Review your weekly progress
#3.Friday at 6:00 PM: Weekly work completed
#Use:
#1.schedule.every().monday.at(...)
#2.schedule.every().wednesday.at(...)
#3.schedule.every().friday.at(...)


import time
import schedule

def MondayTask():
    print("Start your weekly goals")

def WednesdayTask():
    print("Review your weekly progress")

def fridayTask():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(MondayTask)

    schedule.every().wednesday.at("17:00").do(WednesdayTask)

    schedule.every().friday.at("18:00").do(fridayTask)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()

