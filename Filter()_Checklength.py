#write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

Checklength = lambda s : len(s)>5

def main():
    Data = input("Enter String seperated by space : ").split()

    FData = list(filter(Checklength,Data))

    print("Strings having length greater than 5: ",FData)

if __name__ == "__main__":
    main()