#Write a Python program that reads and displays the contents of a specified text file every minute.
#Handle the following conditions:
#1.File does not exist
#2.File is empty
#3.Permission is denied
#4.File cannot be opened


import os
import schedule
import time

def Readfile():

    Filepath = input("Enter a file path: ")

    if not os.path.exists(Filepath):
        print("File does not exist")
        return

    try:

        fobj = open(Filepath, "r")
        Data = fobj.read()

        if len(Data)==0:
            print("File is empty")
        else:
            print("\nFile Contents: ")
            print(Data)

        fobj.close()

    except PermissionError:
        print("Permission is denied")

    except OSError:
        print("File cannot be opened")


def main():
    schedule.every().minute.do(Readfile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()