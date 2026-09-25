
# copy list
numbers = [10, 20, 30,40,50]
new_num = numbers.copy()

new_num.append(24)
new_num.pop(1)

print(new_num)
print(numbers)




# second largest
numbers.sort()
print(numbers[-2])



# second smallest
print(numbers[1])



# reverse
print(numbers[::-1])



# removing duplicates
lis1 = [1, 2, 2, 3, 4, 4, 5, 5]
lis2 = []

for n in lis1:
    if n not in lis2:
        lis2.append(n)

print(lis2)


# counting freq of elements
lis3 = []
for n in set(lis1):
    lis3.append(lis1.count(n))

print(lis3)


# predict output
num = [10, 20, 30, 40, 50]
print(num[-3:])

# INDEXING
num[2] = 100
print(num)



num[0:3] = 1,2,3
print(num)


# |         | Indexing      | Slicing            |
# | ------- | ------------- | ------------------ |
# | Purpose | One element   | Multiple elements  |
# | Syntax  | `list[index]` | `list[start:stop]` |
# | Example | `numbers[2]`  | `numbers[1:4]`     |
# | Result  | `30`          | `[20,30,40]`       |
