array=[]
number = 0
while True:
    number = input(print("enter int number or # for exit"))

    if number =="#":
        break
    else:
        array.append(int(number))

    if array == sorted(array):
        print("✅",array,"✅")
    elif array !=sorted(array):
        print("❌",array,"❌")
    



    




