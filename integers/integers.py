from random import randint
guesses = 1
number = randint(1,100)

guess = int(input("Guess a number between 1 and 100."))

while guess != number:
    if guess <  number:
        print("your guess is very low ")
        guess = int(input("guess again"))
        guesses = guesses + 1
    elif guess > number:
        print("your guess is very high")
        guess = int(input("guess again"))
        guesses = guesses + 1

print()
print("congrats, you guessed the correct number!")
print("it only took you", guesses, "guesses!")
