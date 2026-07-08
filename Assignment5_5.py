#Design a Python application that creates two threads named Thread1 and Thread2.
#1. Thread1 should display numbers from 1 to 50.
#2.Thread2 should display numbers from 50 to 1 in reverse order.
#3.Ensure that:
#    - Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization.

import threading

def Thread1():
    print("Thread1 Output:")
    for i in range(1, 51):
        print(i)

def Thread2():
    print("Thread2 Output:")
    for i in range(50, 0, -1):
        print(i)

def main():

    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)

    t1.start()
    t1.join()      # Wait until Thread1 finishes

    t2.start()
    t2.join()      # Wait until Thread2 finishes

    print("Exit from Main")

if __name__ == "__main__":
    main()
