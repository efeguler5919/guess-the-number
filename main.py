import random

def play_game():
    print("Guess the Number!")
    number = random.randint(1, 100)
    guesses = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            guesses += 1

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {guesses} tries.")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == 'y' :
        play_game()
play_game()