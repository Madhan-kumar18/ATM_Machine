print("(((((((( Welcome To Our ATM ))))))))")
print("Insert Your Card")
print("Select Your Option")

pin = 1234
totalAmount = 50000
accountNumber = 123456789

print("\n1. Deposit\n2. Withdraw\n3. Balance Check")
option = int(input("Select an option (1/2/3): "))

if option == 1:  
    depositAmount = int(input("Enter Your Amount to Deposit: "))
    
    if depositAmount > 0:
        depositPin = int(input("Enter Your PIN: "))
        if depositPin == pin:
            totalAmount += depositAmount
            print("Deposit Successful! Your New Balance:", totalAmount)
        else:
            print("Wrong PIN!")
    else:
        print("Invalid Deposit Amount!")

elif option == 2:  
    print("Enter Your Amount Between 500 To 50000")
    print("\n1. 10,000\n2. 30,000\n3. 50,000\n4. Other Amount")
    
    withdrawOption = int(input("Select an option (1/2/3/4): "))
    
    if withdrawOption == 1:
        withdrawAmount = 10000
    elif withdrawOption == 2:
        withdrawAmount = 30000
    elif withdrawOption == 3:
        withdrawAmount = 50000
    elif withdrawOption == 4:
        withdrawAmount = int(input("Enter Your Amount: "))
        if withdrawAmount < 500 or withdrawAmount > 50000:
            print("Invalid Amount! Please withdraw between 500 and 50000.")
            exit()
    else:
        print("Invalid Option!")
        exit()
    
    withdrawPin = int(input("Enter Your PIN: "))
    
    if withdrawPin == pin:
        if withdrawAmount <= totalAmount:
            totalAmount -= withdrawAmount
            print("Collect Your Cash.")
            print("Remaining Balance:", totalAmount)
        else:
            print("Insufficient Balance!")
    else:
        print("Wrong PIN!")

elif option == 3:  
    checkPin = int(input("Enter Your PIN: "))
    if checkPin == pin:
        print("Your Current Balance:", totalAmount)
    else:
        print("Wrong PIN!")

else:
    print("Invalid Option! Please Try Again.")
