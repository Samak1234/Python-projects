import random #

secret = random.randint(1,100)
guess = int(input("Guessa number between 1 and 100: "))

if guess == secret:
    print("Congratulations,Correct")
elif guess < secret:
    print("Guess Higher number")
else:
    print("Guess lower number")