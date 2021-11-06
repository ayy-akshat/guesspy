from random import randint as r
n = r(1, 9)
chances = 5
print("guessing game\n\n")
while True:
    if (chances <= 0):
        print("you ran out of chances. the number was " + str(n) + "\n\nnow play again\n")
        chances = 5
        n = r(1, 9)
        continue
    i = input("you have " + str(chances) + " chance[s] to guess between 1-9: ")
    try:
        int(i)
    except:
        print("please enter an integer")
        continue
    if (not 1 <= int(i) <= 9):
        print("between 1 and 9")
        continue
    chances -= 1
    if (int(i) > n):
        print(str(i) + " is too high")
    elif (int(i) < n):
        print(str(i) + " is too low")
    else:
        print("\ncongratulations: you guessed " + str(i) + " correctly\n\nnow play again\n")
        chances = 5
        n = r(1, 9)
