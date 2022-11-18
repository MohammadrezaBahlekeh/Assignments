import random 

computersocre = 0
userscore = 0

print("choose one of this (rock - paper - scissors)")

while userscore<=3 or computersocre<=3:

    x=random.randint(1,3)

    if x == 1:
        computerchoice = "rock"

    elif x == 2:
        computerchoice = "paper"

    elif x == 3:
        computerchoice = "scissors"  
    
    userchoice = input("choose : ")

    print("😎 : ",userchoice)
    print("💻 : ",computerchoice)

    if userchoice == "rock" and computerchoice == "scissors":
        userscore = userscore + 1

    elif userchoice == "paper" and computerchoice == "rock":
        userscore = userscore + 1

    elif userchoice == "scissors" and computerchoice == "paper":
     userscore = userscore + 1

    elif computerchoice == "rock" and userchoice == "scissors":
     computersocre = computersocre + 1

    elif computerchoice == "paper" and userchoice == "rock":
        computersocre = computersocre + 1

    elif computerchoice == "scissors" and userchoice == "paper":
        computersocre = computersocre + 1

    elif computerchoice == "rock" and userchoice == "rock":
     print("draw")

    elif computerchoice == "scissors" and userchoice == "scissors":
        print("draw")    

    elif computerchoice == "paper" and userchoice == "paper":
        print("draw")

    elif computerchoice == "rock" and userchoice == "rock":
        print("draw")

if userscore == 3 :
     print ("you won !! sib migholi??🍏")
    

elif computersocre == 3 :
    print ("you lost !! bayad sib bogholi !!🍏")