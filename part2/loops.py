# ----------WHILE LOOP----------------

# i = 1

# while(i<=5):
#     print(i)
#     i+=1

# -----------------------

# j = 5
# while(j>=1):
#     print(j)
#     j-=1

# -----------------------

# k = 1
# while(k<=10):
#     print(2*k)
#     k+=1

# -----------------------

# i = 1
# while(i<=21):
#     if(i%2==1):
#         i+=1
#         continue
#     print(i)
#     i+=1

# -----FOR LOOP--------------

sum = 0
n = int(input("Enter number: "))
for i in range(1,n+1):
   sum +=i
print("Sum of n Natural numbers is ", sum)

# ---------------------

word = "naziya"

count = 0
for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
     count+=1


print("Number of vowels in the word is ", count)