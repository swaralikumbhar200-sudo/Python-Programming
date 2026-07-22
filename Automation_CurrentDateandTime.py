#Write a Python program that displays the current date and time after every one minute.
#Use the datetime module.
#Expected Output (Example):
#Current Date and Time: 25-07-2026 04:30:00 PM


import schedule
import datetime
import time

def Display():
    print("Current Date and Time is: ", datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()