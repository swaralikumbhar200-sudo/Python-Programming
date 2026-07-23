#Write a program that accepts:
#1.A message from the user
#2.A time interval in seconds
#Schedule the program to display the message repeatedly after the specified interval.
#Example input: Enter message: Jay Ganesh, Enter interval in seconds: 5
#Expected output: Jay Ganesh
#(repeated every five seconds)
#Note: Validate that the interval is greater than zero.


import schedule
import time

Message= input("Enter a message from user: ")
Time = int(input("Enter interval in seconds: "))


def Display():
    print(Message)
    

def main():
    if Time>0:
        schedule.every(Time).seconds.do(Display)
    else:
        print("Invalid interval")
        return

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()