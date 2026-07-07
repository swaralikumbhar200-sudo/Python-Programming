# write a program which accept number from user and check whether that number is positive, negative or zero. 
# input =8 , output = Positive number, # input =-11 , output = Negative number, # input =0 , output =Zero

n = int(input("Enter a number: "))

def main():
  if n > 0:
    print("Postive Number")
  elif n < 0:
    print("Negative Number")
  else:
    print("Zero")

if __name__ == "__main__":
  main()