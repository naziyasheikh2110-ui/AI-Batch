n = 10

while(True):
 user_num = int(input("Guess the number: "))
 if(user_num>n):
    print("Too High ! try again")
 elif(user_num<n):
   print("Too Low")
    
 else:
   print("Correct")
   break
  
