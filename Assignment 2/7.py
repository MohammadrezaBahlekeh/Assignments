fibonumber = int(input("enter the fibonacci sequence : "))

a = 1
b = 0

for i in range(fibonumber):

    result = a + b
    a = b
    b = result
    
    print(result)    