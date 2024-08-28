import random 

def main():

    guess = -1
    answer = random.randint(1,100)
    guesscount = 0

    while guess != answer:
        guess = int(input("pick a number between 1 and 100: "))
        guesscount = guesscount + 1
        if guess > answer:
            print("too high")
        elif guess < answer:
            print("too low")

        if guesscount > 20:
            break

    if guess == answer:
        print("congratulations you guessed it!")
    
    else:
        print("numbers of tries exceeded")

main()