# Program for a simple guessing game

secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 10): "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")

print("Congratulations! You guessed the correct number.")

