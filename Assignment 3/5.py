firstnumber = int(input("firstnumber : "))
secondnumber = int(input("secondnumber : "))
gcd = 0 

if firstnumber > secondnumber:
    temp = secondnumber
else:
    temp=firstnumber

for i  in range(1,temp + 1):
    if((firstnumber % i == 0)) and (secondnumber % i == 0):
        gcd = i

print("gcd = ",gcd)