import random
guess = random.randint(1, 100)
ans = "n"
count += 1
while ans !="y":
    print("i guess", guess)
    ans = input("is that right? type y for yes, h if my guess is too high, or l if my answer is too low.")
    if ans == "y":
        print("yay! that took me",count, "tries")
        break
    elif ans == "h":
        guess = random.randint(int(prevGuess),int(guess))
        count += 1
        prevGuess = guess
    else: #guess too low
        guess = random.randint(int(guess),int(prevGuess))
    count += 1
    prevGuess = guessss
