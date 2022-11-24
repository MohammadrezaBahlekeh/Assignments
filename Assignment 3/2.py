import random 

lnumber = int(input("enter the lenth"))
lowestnumber = int(input("enter the lowest number"))
highestnumber = int(input("enter the highest number"))

radnomnumber = []

for i in range (lnumber):
    radnomnumber.append(random.randint(lowestnumber,highestnumber))

print (radnomnumber)
