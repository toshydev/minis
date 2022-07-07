# Numb3rs - a number guessing game

from random import randint

print("\nWelcome to Numb3rs!\n")

# Select difficulty
print("Select difficulty:")
print("1.\teasy\n2.\tmedium\n3.\thard")
while True:
    difficulty = int(input())
    if difficulty == 1:
        number = randint(1, 20)
        print("\nGuess a number between 1 and 20")
        break
    if difficulty == 2:
        number = randint(1, 50)
        print("\nGuess a number between 1 and 50")
        break
    if difficulty == 3:
        number = randint(1, 100)
        print("\nGuess a number between 1 and 100")
        break
    else:
        print("Enter 1 for 'easy', 2 for 'medium', 3 for 'hard'")

# Take guesses
for guessesTaken in range(1, 7):
    userGuess = int(input())
    if userGuess < number:
        print("Too low.")
    elif userGuess > number:
        print("Too high.")
    else:
        break

# Win or lose
if userGuess == number:
    print(f"Correct! You guessed the number in {guessesTaken} guesses.")
else:
    print(f"Game Over. The number was: {number}")

print("\nThank you for playing Numb3rs")