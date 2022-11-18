hour = 0
minute = 0
second = 0

print("enter the time")

hour = int(input("hour : "))
minute = int(input("minute : "))
second = int(input("second : "))

time = (hour*3600) + (minute*60) + second

print(hour ,":",minute,":",second)
print(time)
