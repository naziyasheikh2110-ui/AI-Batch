# Given:

t = (10, 20, 30, 40, 50)

# Check whether 30 exists.

if 30 in t:
    print("Yes, it exist")


# Check whether 100 does not exist.

if 100 not in t:
    print("Doesn't Exist")

# Take a number from the user and check whether it exists in:

num = int(input("Enter the number: "))

if num in t:
    print("Yes, it exist")
else:
    print("Doesn't Exist")