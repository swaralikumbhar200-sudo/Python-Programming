#Design a Python application that creates two threads.
#1. Thread 1 should calculate and display the maximum element from a list.
#2. Thread 2 should calculate and display the minimum element from the same list.
#3. The list should be accepted from the user.

import threading

def Maximum(data):
    print("Maximum element is:", max(data))


def Minimum(data):
    print("Minimum element is:", min(data))


def main():
    arr = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=Maximum, args=(arr,))
    t2 = threading.Thread(target=Minimum, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")


if __name__ == "__main__":
    main()