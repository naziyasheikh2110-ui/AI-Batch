# ------------------que1-------------------

# salary = int(input("Enter your salary: "))

# if salary<=3000:
#     print("you have to pay 5% taxes")
# elif salary>3000 and salary<=70000:
#     print("you have to pay 15% taxes")
# else:
#     print("you have to pay 25% taxes")

 # --------------que2--------------------
# def printSalary(a,b):  
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)

# printSalary(1,10)
    
# ---------------que3-------------------
# def printDigit(num):

#    n=(len(str(num)))

#    for i in range(1,n+1):
#      print(int(num%10))
#      num/=10

# printDigit(123)

# ---------------que4-----------------

# def count(num):
#     print(len(str(num)))

# count(1234)

# # ------------que5--gltt----------------
def sum(digit):
 total = 0
 
 while(digit>0):
    n = digit%10
    total+=n
    digit = digit/10

 return int(total)
   
print(sum(123))

# -----------------que6--------------
# def printNum():
#     for i in range(1,101,1):
#         if(i%3 == 0 and i%5==0):
#             print(i)
# printNum()

# ----------------que7-----------------
# while(True):
#    user = int(input("Enter number n: "))

#    if user == "quit":
#        print("User quit the game")
#        break
#    else:
#        user = int(user)
#        print(user)

# --------------que9----------------------
# def is_prime(n):
#     if n == 2:
#         return True
#     else:
#         for i in range(2,n,1):
#           if n%i != 0:
#               return True
#           else:
#               return False

# print(is_prime(3))
   