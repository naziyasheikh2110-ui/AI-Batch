tup = (10, 20, 30, 40, 50)


sum=0
largest=tup[0]
smallest=tup[0]


for t in tup:
    print(t)
    sum+=t
    if(t>largest):
        largest=t
    elif(t<smallest):
        smallest=t
 

print("Sum of tuple element:",sum)
print("Largest Element:",largest)
print("Smallest Element:",smallest)




tup2 = (10, 15, 22, 31, 40, 55, 60)

evenCount = 0
even = ()

for i in tup2:
     if(i%2==0):
        evenCount+=1
        even = even+(i,)

print("Even Count:", evenCount)
print("Tuple with Even number:",even)