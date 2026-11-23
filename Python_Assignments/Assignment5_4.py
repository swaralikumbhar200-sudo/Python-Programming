# Design a Python application that creates three threads named Small, Capital, and Digits.
#1. All threads should accept a string as input.
#2. The Small thread should count and display the number of lowercase characters.
#3. The Capital thread should count and display the number of uppercase characters.
#4. The Digits thread should count and display the number of numeric digits.
#5. Each thread must also display:
#   - Thread ID
#  - Thread Name

import threading

def Small(s):
    count = 0

    for ch in s:
        if ch.islower():
            count = count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of lowercase characters:", count)
    print()


def Capital(s):
    count = 0

    for ch in s:
        if ch.isupper():
            count = count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of uppercase characters:", count)
    print()


def Digits(s):
    count = 0

    for ch in s:
        if ch.isdigit():
            count = count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of digits:", count)
    print()


def main():
    str1 = input("Enter a string: ")

    thread1 = threading.Thread(target=Small, args=(str1,), name="Small")
    thread2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
    thread3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()