import random

wordsBank = ["case","motherboard","gpu","keyboard","mouse","mousepad","desk","cpu","headphone"]

usermistakes = 0
goodchar = []
badchar = []

word = random.choice(wordsBank)

while usermistakes<6 :

    for i in range (len(word)):

        if word[i] in goodchar:
            print(word[i],end="")
        else:
            print("_ ",end="")

    userchar = input("guess : ").lower()

    if len(userchar) ==1 :

        if userchar in word :
            goodchar.append(userchar)
            goodchar.append(userchar)
        else:
            badchar.append(userchar)
            usermistakes +=1
    else :
        print(":|")

if usermistakes == 6:
    print("GAME OVER!!")
if goodchar == word:
    print("you win")
    print(word)
    
#شرط برنده شدن پیاده سازی نشده است