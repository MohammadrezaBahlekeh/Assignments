import random

number = random.randint(1,20)
counter =0
for i in range (10):
    guessednumber = int(input("Guess : "))

    if number == guessednumber:
        counter =counter +1
        print("you won the game with ",counter," Guess")

    elif guessednumber > number:
        counter =counter +1
        print("guess the lower number")

    elif guessednumber < number :
        counter =counter +1
        print("guess the higher number")

if counter == 10 :
    print("GAME OVER!!")