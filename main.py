import random

guess_number = random.randint(1, 100)

low = 1
high = 100

attempts = 0

running = True

while running:
    user_input = (input("Guess a number between (1 and 100) and 'hint' to take a hint': "))
    attempts += 1
    
    if user_input.lower() == "hint":
        print(f"The number is between {low} and {high}.")
        continue
    
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(user_input)
    
    if guess == guess_number:
        print(f"Congratulations! You guessed the number: {guess_number} in {attempts} attempts.")
        running = False
    else:
        print(f"Too {"low" if guess < guess_number else "high"}! Try again.")
        print(f"Attempts: {attempts}\n")
        low = guess if low < guess < guess_number else low
        high = guess if guess_number < guess < high else high        
        
    print(f"The number is between {low} and {high}.") if attempts == 3 else None