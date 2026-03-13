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
        print(f"Too {"low" if guess < guess_number else "high"}! Try again.")
        print(f"Attempts: {attempts}\n")