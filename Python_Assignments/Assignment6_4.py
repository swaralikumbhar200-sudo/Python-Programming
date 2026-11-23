# Design a Python application that creates two threads.
#1. Thread 1 should compute the sum of elements from a list.
#2. Thread 2 should compute the product of elements from the same list.
#3. Return the results to the main thread and display them.

import threading

def Sum(data):
    total = 0

    for i in data:
        total = total + i

    print("Sum =", total)


def Product(data):
    pro = 1

    for i in data:
        pro = pro * i

    print("Product =", pro)


def main():
    arr = list(map(int, input("Enter numbers: ").split()))

    thread1 = threading.Thread(target=Sum, args=(arr,))
    thread2 = threading.Thread(target=Product, args=(arr,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from Main")


if __name__ == "__main__":
    main()