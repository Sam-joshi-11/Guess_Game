# 🎮 Guess the Number Game (Day 9 Project)

import random

# Step 1: Welcome the player
name = input("Enter your name: ")
print(f"\n👋 Welcome, {name}!")
print("I’m thinking of a number between 1 and 10.")
print("You have 3 chances to guess it.\n")

# Step 2: Generate the secret number
secret_number = random.randint(1, 10)

# Step 3: Give the player 3 attempts
for attempt in range(1, 4):
    try:
        guess = int(input(f"🔢 Attempt {attempt}: Your guess? "))
        
        if guess == secret_number:
            print(f"\n🎉 Correct! Well done, {name}!")
            break
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")
    
    except ValueError:
        print("❌ Please enter a valid number!")

# Step 4: After loop ends (if not guessed)
else:
    print(f"\n😢 Sorry, {name}. The number was {secret_number}. Better luck next time!")