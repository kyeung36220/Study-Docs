balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n): #can read global variable but can't change variable
    global balance #can edit global now
    balance += n

def withdraw(n):
    global balance
    balance -= n





if __name__ == "__main__":
    main()
