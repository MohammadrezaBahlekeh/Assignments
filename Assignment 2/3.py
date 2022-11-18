print ("enter your numbers")

counter = 0
sum = 0
while 1==1 :

    number = input("enter a number and for exit type it")
    if number == "exit" :
        break
    else:
         sum += float(number)
         counter +=1 
    
    average = sum/counter
    print ("your average is : " , average)
        




    