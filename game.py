#number guessing game
import random
number=random.randint(1,100)
attempts=0
while True:
    guess=int(input("Guess a your guess(1-100:"))
    attempts+=1
    if guess==number:
        print("You win! It took", attempts, 'attempts!')
        break
    elif guess!=number:
        if guess>number:
            print("Your guess is too high")
        elif guess<number:
            print("Your guess is too low")
        
