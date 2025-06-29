def clear_screen():
    print("\n" * 50)

print("🎮 Welcome to Multiplayer Guess Game")
print("👤 Player 1: Please enter a secret number (1 to 100)")
secret_number = int(input("👉 Player 1, enter the number: "))

clear_screen()
print("👤 Player 2: It's your turn to guess!")
attempts = 3

for i in range(1, 4):
    guess = int(input(f"🔢 Attempt {i}: Your guess? "))
    if guess == secret_number:
        print("🎉 You got it! Player 2 wins!")
        break
    elif guess < secret_number:
        print("📉 Too low!")
    else:
        print("📈 Too high!")

else:
    print(f"💥 Out of chances! The correct number was {secret_number}")
    print("Player 1 wins!")