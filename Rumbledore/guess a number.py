import random

is_playing = True
score = 0


while is_playing:

    rnd_num = random.randint(1, 51)

    print("---------- Welcome to Rumblesore's guess game ----------")
    answer = int(input("Guess a number between 1-50: \n"))

    if rnd_num == answer:
        print("You guessed right!")
        score += 1

    else:
        print("Incorrect!")
        if answer > rnd_num:
            print("guess lower")
        else:
            print("guess higher")

    answer = input("Wanna play again? (yes/no)\n")
    if answer == "yes":
        continue
    else:
        is_playing = False

