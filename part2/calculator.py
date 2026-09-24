def calculator(a,b,operation):
    if(operation== '+'):
      print(a+b)
    elif(operation == '-'):
      print(a-b)
    elif(operation=='*'):
      print(a*b)
    elif(operation== '/'):
       print(a/b)
    elif(operation=='%'):
       print(a%b)
    else:
       print("Incorrect syntax !")

calculator(2,1, 'e')