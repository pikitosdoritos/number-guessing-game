import random
import json
import os

FILE="record.json"

guess_number = random.randint(1, 100)

low = 1
high = 100

attempts = 0

running = True

def save_record(name, attempts, level):
    if not os.path.exists(FILE):
        data = []
    else:
        with open(FILE, "r") as f:
            data = json.load(f)
            
    data.append({
        "name": name,
        "attempts": attempts,
        "level": level,
    })
    
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_record():
    with open(FILE, "r") as f:
        data = json.load(f)
        
    data = sorted(data, key=lambda x: x["attempts"], reverse=True)
    
    return data

def print_record():
    records = get_record()
    
    print("\nTABLE OF RECORDS")
    print("-----------------")

    for i, r in enumerate(records[:10], start=1):
        print(f"{i}. {r['name']} - {r['score']}")

def select_level_and_name():
    while True:
        name = input("Enter your name: ")
        
        if not name.isalpha():
            print("Please enter a valid name.") 
            continue
        
        select_level = input("Select a level: 'easy', 'medium', 'hard': ")
            
        if select_level.lower() == "easy":
            max_attempts = 10
            break
        elif select_level.lower() == "medium":
            max_attempts = 7
            break
        elif select_level.lower() == "hard":
            max_attempts = 5
            break
        else:
            print("Invalid level. Please choose 'easy', 'medium', or 'hard'.")
            
    print(f"You have {max_attempts} attempts to guess the number.")
            
    return name, select_level, max_attempts

name, selected_level, max_attempts = select_level_and_name()
  
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
        save_record(name, attempts, selected_level)
        running = False
    
    elif attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {guess_number}.")
        running = False
        
    else:
        print(f"Too {"low" if guess < guess_number else "high"}! Try again.")
        print(f"Attempts: {attempts}\n")
        low = guess if low < guess < guess_number else low
        high = guess if guess_number < guess < high else high        
        
    print(f"The number is between {low} and {high}.") if attempts == 3 else None