
# Tuple -> List
tup = (10, 20, 30, 40)
lis = list(tup)
print(lis)


# list -> tuple
lis_num = [10, 20, 30, 40]
tup1 = tuple(lis_num)
print(tup1)

# Modifing tuple
t = (10, 20, 30)

l = list(t) # tuple -> list 
l.insert(2,100) #list moodify 

t = tuple(l)  #again list -> tuple

print(t) #tuple modified in directly