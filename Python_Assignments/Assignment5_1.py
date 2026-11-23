#Design a Python application that creates two separate threads named Even and Odd.
#1.The Even thread should display the first 10 even numbers.
#2.The Odd thread should display the first 10 odd numbers.
#3.Both threads should execute independently using the threading module.
#4.Ensure proper thread creation and execution.


import threading

def Even(no):
    print("Even numbers: ")
    for i in range(2,no,2):
        print(i)
       

def Odd(no):
   print("Odd numbers: ")
   for i in range(1,no,2):
        print(i)
       
    
def main():
   n=20
    
   thread1 = threading.Thread(target= Even, args =(n,))
   thread2 = threading.Thread(target= Odd, args =(n,))

   thread1.start()
   thread2.start()

   thread1.join()
   thread2.join()

if __name__ =="__main__":
   main()
