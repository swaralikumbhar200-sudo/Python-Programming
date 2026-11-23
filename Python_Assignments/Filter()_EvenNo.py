# write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

EvenNumber= lambda No : No%2 == 0

def main():
    Data = list(map(int,input("Enter nos: ").split()))
    FData = list(filter(EvenNumber,Data))
    print("Data after filter: ",FData)
  
if __name__ =="__main__":
    main()