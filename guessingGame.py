import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Please guess a number between 1 and 9 ")

while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations On Your Victory!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances == 1

if not chances < 5:
    print("Sorry you have lost. Try again")