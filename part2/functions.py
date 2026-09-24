# def hello():
#     print("Hello world")

# hello() 

# def sum(a,b):
#     s = a+b
#     return s

# print(sum(2,3))

# def avg(a,b,c):
#     a = (a+b+c)/3
#     return a

# print(avg(3,4,2))

def fac(n):
    f = 1
    for i in range(1, n+1):
        f*=i
        
    return f

print(fac(2))
