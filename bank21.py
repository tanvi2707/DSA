accountbalance=10000


balance=int(input("Enter Amount:"))
operation=input("Press D for Deposit and W for Withdrawal or E to Exit:")



if (operation=='d'):
     accountbalance=accountbalance+balance
     print("New Balance is:",accountbalance)

elif (operation=='w'):
     if (accountbalance<balance):
         print("Inssuficient Balance")
         
     else:
         accountbalance=accountbalance-balance
         print("New Balance is:",accountbalance)
     
else:
     print("Invalid.Press D for Deposit and W for Withdrawal:")   
     
       
    
    



