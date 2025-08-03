import random

def choose_difficulty():
    print("🎯 Choose difficulty level:")
    print("1. Easy (1–20)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return random.randint(1, 20), 7
        elif choice == '2':
            return random.randint(1, 50), 10
        elif choice == '3':
            return random.randint(1, 100), 12
        else:
            print("⚠️ Invalid input. Please enter 1, 2, or 3.")

def play_game():
    number, max_attempts = choose_difficulty()
    guesses = 0

    while guesses < max_attempts:
        try:
            guess = int(input(f"\n🔢 Guess the number ({guesses+1}/{max_attempts}): "))
            guesses += 1

            if guess == number:
                print(f"🎉 Correct! You guessed the number {number} in {guesses} attempts.")
                break
            elif guess > number:
                print("🔽 Lower number please!..")
            else:
                print("🔼 Higher number please!..")

            # Smart Hint
            diff = abs(guess - number)
            if diff >= 20:
                print("🔥 You're way off!")
            elif diff <= 5:
                print("💡 You're very close!")

        except ValueError:
            print("❌ Please enter a valid number!")

    else:
        print(f"\n❌ You've used all {max_attempts} attempts. The number was {number}.")

def main():
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

main()
