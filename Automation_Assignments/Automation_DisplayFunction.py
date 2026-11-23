#Write a Python program that schedules a function to print:
#Coding Kar..!
#every 30 minutes.

import time
import schedule

def Display():
    print("Coding Kar..!")

def main():
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()