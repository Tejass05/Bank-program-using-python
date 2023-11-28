accno = 0
amount = 0
Balance = 0
while True:
  print("-------Welcome to Bank-------")
  print("1.Create Account \n 2.Credit Amount \n 3.Debit Amount \n 4.Show Balance \n 5. Exit")
  choice = int(input("Enter your Choice : "))
  if(choice == 1):
        name =input("Enter your name : ")
        amount = int(input("Enter the amount : "))
        if(amount >= 1000) :
            Balance = amount
            print("Your Account has been created and your acccount number is 1111")
            accno = 1111
        else:
            print("To create account amount must be more than 1000")   
  elif (choice == 2 ):
        bankAccount = int(input("Enter Bank Account Number : "))
        if bankAccount == accno :
            creditAmount = int(input("Enter Amount : "))
            Balance = amount + creditAmount 
            print(f"{creditAmount} Amount Has been Credited")
        else:
            print ("Invalid Account Number ! Please enter correct account number") 
  elif(choice == 3):
       bankAccount =int(input("Enter Bank Account Number : "))
       if bankAccount == accno :
            DebitAmount = int(input("Enter Amount : "))
            if(DebitAmount >= amount):
                 print("Low amount")
            else:
                Balance = amount - DebitAmount 
                print(f"{DebitAmount} Amount Has been debited")
       else:
            print ("Invalid Account Number ! Please enter correct account number") 
  elif(choice == 4):
       bankAccount = int(input("Enter Bank Account Number : "))
       if bankAccount == accno :
            print(f"Your Current Balance is {Balance}")
       else :
            print ("Invalid Account Number ! Please enter correct account number")
  elif(choice == 5):
       break
  else:
       print("Invalid Choice ! Please enter write Choice")
                