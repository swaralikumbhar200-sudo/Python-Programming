#Create a task that executes every day at 9:00 AM and prints:
#Namskar...
#Use:
#schedule.every().day.at("09:00").do(...)

import schedule
import time

def Everyday():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(Everyday)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()