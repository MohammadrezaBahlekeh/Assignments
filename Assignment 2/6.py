import random 

dicenumber = random.randint(1,6)
while 1==1:
    if dicenumber == 6 :
        print("🎲",dicenumber)
        print("bonus")
        dicenumber= random.randint(1,6)
    else :
        print("🎲",dicenumber)
        break

