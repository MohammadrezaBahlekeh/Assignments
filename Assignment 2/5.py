print("second to hour")

time = int(input("enter the second : "))

hour = (time//3600)

temp = (time % 3600)
minute = (temp//60)

second = temp % 60

print (hour,":",minute,":",second)