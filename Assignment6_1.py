# Design a Python application that creates two threads named Prime and NonPrime.
#1. Both threads should accept a list of integers.
#2. The Prime thread should display all prime numbers from the list.
#3. The NonPrime thread should display all non-prime numbers from the list.


import threading

def isPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False
    return True


def Prime(data):
    print("Prime Numbers:")
    for i in data:
        if isPrime(i):
            print(i)


def NonPrime(data):
    print("Non-Prime Numbers:")
    for i in data:
        if not isPrime(i):
            print(i)


def main():
    arr = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=Prime, args=(arr,))
    t2 = threading.Thread(target=NonPrime, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")


if __name__ == "__main__":
    main()
