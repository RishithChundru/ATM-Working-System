#ATM Machine Project using Python
#START OF THE PROGRAM
#Welcome page
print("Welcome to SRT ATM!")
#Inserting ATM Card and logging-in with crediantials 
start = "Please insert your Card"
print(start)
#Correct pin with which the user can login successfully to make transactions
act_pin = 2005
#Asking user to enter ATM Pin
enter_pin = int(input("Please enter your 4-digit secret pin: "))
#Minimum Balance to be kept in bank
min = 5000
#Cuurent Balance in the user's account before transactions
Amt = 50000
#If the entered pin i.e.enter_pin matches the given correct pin i.e. act_pin matches,the Machine will display user's details and the balance available in the user's account.
if enter_pin == act_pin:
     print("Hello Mr.John")
     print("Your current balance is:",Amt)
     #Asking user to choose service to make Transaction
     #If the user press 1 then the machine makes user to deposit money 
     # If the user press 2 then the machine makes user to withdraw money
     # If the user press 3 then the machine displays the available balance in the Account
     #If the user press 4 then the machine makes user to change existing pin #
     #If the user press 5 then the user can make Fund Transfer to any account through ATM Machine.
     print('''
               CHOOSE YOUR SERVICE
          \t\t\tPRESS 1 to DEPOSIT Money
          \t\t\tPRESS 2 to WITHDRAW Money
          \t\t\tPRESS 3 for Balance Enquiry
          \t\t\tPRESS 4 to Change your ATM pin
          \t\t\tPRESS 5 for Fund Transfer
          ''')
     #The machine asks  user to press desired option mentioned above
     option = int(input("Select an option: "))
     if option == 1:
          print("Deposit Money into your Account") #if the user chose option 1 then the machine give access to the user to deposit money
          Dep = int(input("Enter the Amount: Rs. ")) #Entering Depositing Money
          Amt+=Dep #Adding Previous Balance and Deposited Money
          print("Please wait while Transaction is being processed")
          print("Amount is successfully deposited into your Bank Account") #Displays this msg after successful deposition
          print("Total Balance after the transaction: Rs.",Amt) #Updated Balance after deposition of money by adding previous balance and deposited money                                                                                                                                     
          print("Thank you!\nVisit Again") 
     elif option == 2:
          print("WITHDRAW WISHED AMOUNT") #If the user chose option 2 the machine give access to the user to withdraw wished amount
          Wtd = int(input("Enter Amount: Rs.")) #Entering Withdraw Amount
          Amt-=Wtd #Subtracting Previous balance with Withdrawn amount
          if Amt<min: 
               print("Amount can't be withdrawn due to exceeding of Minimum Limit") #If the balance after withdrawing of money exceeds minimum limit of account then the amount can't be withdrawn and the machine displays the mentioned msg in the print function
          else:
               print("Please wait while Transaction is being processed")
               print("Amount is successfully withdrawn from the Account")
               print("Total Balance after the transaction: Rs.",Amt) #if minimum limit won't be exceeding after withdrawing money the machine gives money and the total balance after the transaction will be displayed by subtracting previous balance with withdrawn amount
               print("Thank you!\nVisit Again")
     elif option == 3:
          print("Please wait while Transaction is being processed")
          print("Current Balance: Rs.",Amt) #if the user chose option 3 then the machine displays the total balance available in the account
          print("Thank you!\nVisit Again")
     elif option == 4:
          print("Change your ATM pin") #if the user chose option 4 the machine give access to the user to change his/her ATM-Pin but the changed pin can't be used to login into his/her account in the next run
          new_pin = int(input("Enter your new Secret Pin: ")) #Machine asks user to enter new pin
          aga_new = int(input("Enter your new Secret Pin again: ")) #Machine asks user to confirm and the new pin again
          a = str(new_pin)
          b = str(aga_new)
          if len(a)==4 and len(b)==4 and a == b: 
               print("Please wait while Transaction is being processed") #if the lengths of both new and confirmed pins are equal to 4 and they both are same,then the pin will be changed
               print("Pin changed successfully")
          elif len(a) == 4  and len(b)==4 and a!=b:
               print("Entered pins are not matching\nPlease try again") #if the lengths are equal but they aren't same to each other then machine won't change pin
          elif len(a)!= 4 or len(b) != 4:
               print("Pin should contain 4 digits only\nPlease try again") #if the length of any new pins i.e. new or confirmed pins are not equal to 4 then the pin can't be changed
     elif option == 5:
          print("Transfer Fund") #if the user chose option 5 then the machine give access to the user to transfer fund from his/her account
          acc_num=int(input("Enter Payee's Account Number: ")) #machine asks user to enter Payee's Account Number
          tra = int(input("Enter Amount: ")) #machine asks user to enter amount to be transferred
          
          Amt-=tra #Subtracting Previous Balance with transferred amount
          if Amt < min:
               print("Please wait while transaction is being processed")
               print("Fund Transfer has breached Minimum limit\nTransaction not possible\nThank You!") #if the minimum limit will be exceeding after the transfer of fund then the fund can't be transferred and the machine displays the mentioned message which is in print function
          else:
               print("Please wait while Transaction is being processed")
               print("Amount is successfully transfered")
               print("Current Balance:",Amt) #if the minimum limit won't be exceeding after transfer of fund the amount will be successfully transferred and displays the remaining balance in the account by subtraction of previous balance with transferred amount
               print("Thank you\nVisit again!")
     else:
          print("Please choose valid Service\nFor choosing Valid Service,Please start a new session")  #if the user select an option which is not mentioned in the options then the machine will display the message which is given in the print function 
else:
     print("Wrong pin entered by the user\nPlease check and enter valid pin") #if the user enter wrong pin i.e. the pin which is not mentioned in the act_pin variable then the machine will display the message which is assigned in print function
#END OF THE PROGRAM