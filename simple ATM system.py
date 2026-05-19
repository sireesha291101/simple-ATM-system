print("------welcome to ATM------")
balance = 10000
while True:
    print("\n1. Check Balance")
    print("2. Deposite")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("your current balance is: ",balance)
    elif choice == "2":
        deposite = float(input("Enter deposite amount: "))
        if deposite >= 0:
            balance = deposite + balance
            print("Amount deposited successfully")
            print("Your balance is: ",balance)
        else:
            print("Invalid deposite amount")
    elif choice == "3":
        withdraw = float(input("Enter withdraw amount: "))
        if withdraw <= balance and withdraw >0:
            balance = balance-withdraw
            print("please collect your money")
            print("Remaining balance: ", balance)
        elif withdraw > balance:
            print("Insufficient balance")
        else:
            print("Invalid withdrawal amount")
    elif choice == "4":
        print("Thankyou")
        break
    else:
        print("Invalid choice. Please try again")