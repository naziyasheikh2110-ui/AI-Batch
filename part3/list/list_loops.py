# nums = [1,2,3,4]

# for i in nums:
#     print(i)

# val = 3
# idx = 0

# for i in nums:
#     if(i==val):
#         print(idx)
#         break
#     else:
#         idx+=1


# #------------------------------------
# numbers = [5, 10, 15, 20, 25]
# sum=0
# even = 0
# odd = 0

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     print(num)

#     sum+=num

#     if(num%2==0):
#         even+=1
#     else:
#         odd+=1

#     if(num>largest):
#         largest = num

#     if(num<smallest):
#         smallest = num

# print("Total even number = ", even)
# print("Total even number = ", odd)
# print("Sum = ", sum)
# print("Largest = ", largest)
# print("Smallest = ", smallest)


# list1 = [1,2,3,4,5]
# list2 = []
# list3 = []

# for i in list1:
#     if(i%2==0):
#         list2.append(i)

#     list3.append(i*i)
    
    
# print(list2)
# print(list3)



# NESTED LOOPS
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])

sum = 0
largest = 0
for i in matrix:
    for j in i:
        # print(j)
        sum+=j
        if(j>largest):
            largest = j

       
print(len(matrix))    #row
print(len(matrix[0])) #col
print("Total sum : ", sum)
print("Largest element: " , largest)



