# nums = [1,2,3]

# nums.append(4)
# print(nums)

# nums.insert(2,10)
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# nums.reverse() #list ko reverse krtaa haiiii
# print(nums)  

#  ----------------------------

a = []
for i in range(10,50,10):
    a.append(i)

print(a)



numbers = [10, 20, 30]
numbers.insert(1,15)
print(numbers)



numbers.remove(30) #-> remove number
print(numbers) 



numbers.pop(2) #-> remove number via index 
print(numbers)



# numbers.pop(len(numbers)-1)
numbers.pop() # direct last element remove
print(numbers)



# numbers.append(40)
# numbers.append(50)
# numbers.append(60)
numbers.extend([40,50,60])
print(numbers)



num = [10, 20, 10, 30, 10, 40]
print(num.count(10))


print(num.index(40))


# Ekdum important 3 pairs:

# append  → one item
# extend  → multiple items

# remove  → VALUE
# pop     → INDEX

# count   → kitni baar?
# index   → kahan hai?