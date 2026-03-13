import random

guess_number = random.randint(1, 100)

attempts = 0

running = True

while running:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess == guess_number:
        print(f"Congratulations! You guessed the number: {guess_number} in {attempts} attempts.")
        running = False
    else:
        if guess < guess_number:
            print("Too low! Try again.")
            attempts += 1
        else:
            print("Too high! Try again.")
            attempts += 1