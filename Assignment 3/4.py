snakelen = int(input("enter snake length: "))

for i in range(snakelen):
    if i % 2 == 0:
        print("#", end = "")
    else:
        print("*", end = "")