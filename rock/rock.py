import random
import winsound
import time

# Mapping choices
youDict = {"s": 1, "p": -1, "sc": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissor"}

# Random starting messages
tips = [
    "🎯 Tip: Rock beats Scissors, Scissors beat Paper, Paper beats Rock!",
    "🧠 Strategy: Don't repeat the same move too often!",
    "🔥 Pro Tip: People tend to start with Rock.",
    "😎 Fun Fact: This game is older than computers!"
]

# Sound effect (Windows only)
def beep_result(result):
    if result == "user":
        winsound.Beep(1000, 200)  # Win: High tone
    elif result == "computer":
        winsound.Beep(400, 200)   # Lose: Low tone
    else:
        winsound.Beep(600, 200)   # Draw: Medium tone

# Get and validate user choice
def get_user_choice():
    print("\nChoose your move:")
    print("s  → Stone (Rock)")
    print("p  → Paper")
    print("sc → Scissor")
    choice = input("👉 Your choice (s/p/sc): ").strip().lower()
    if choice not in youDict:
        print("❌ Invalid input! Please enter 's', 'p', or 'sc'")
        return None
    return youDict[choice]

# Decide the round winner
def decide_winner(user, comp):
    if user == comp:
        return "draw"
    elif (user == 1 and comp == 0) or (user == -1 and comp == 1) or (user == 0 and comp == -1):
        return "user"
    else:
        return "computer"

# Play one round
def play_round():
    user = None
    while user is None:
        user = get_user_choice()

    comp = random.choice(list(youDict.values()))
    print(f"\n🧑 You chose: {reverseDict[user]}")
    print(f"💻 Computer chose: {reverseDict[comp]}")

    result = decide_winner(user, comp)
    beep_result(result)  # Play sound

    if result == "draw":
        print("🤝 It's a Draw!")
    elif result == "user":
        print("✅ You Win this round!")
    else:
        print("❌ You Lose this round!")

    return result

# Main game logic
def main():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print(random.choice(tips))  # Show random tip

    rounds = input("🔢 How many rounds would you like to play (best of N)? ")
    try:
        total_rounds = int(rounds)
    except ValueError:
        print("⚠️ Invalid number! Defaulting to 3 rounds.")
        total_rounds = 3

    user_score = 0
    comp_score = 0

    for i in range(1, total_rounds + 1):
        print(f"\n🎲 Round {i} of {total_rounds}")
        result = play_round()
        time.sleep(0.5)

        if result == "user":
            user_score += 1
        elif result == "computer":
            comp_score += 1

    # Final scoreboard
    print("\n📊 Final Scoreboard:")
    print(f"🧑 You: {user_score}")
    print(f"💻 Computer: {comp_score}")

    if user_score > comp_score:
        print("🏆 Congratulations! You won the game!")
    elif comp_score > user_score:
        print("😢 Better luck next time!")
    else:
        print("🤝 It's a tie overall!")

    # Replay option
    again = input("\n🔁 Do you want to play again? (y/n): ").lower()
    if again == 'y':
        print("🔄 Restarting game...\n")
        time.sleep(1)
        main()
    else:
        print("👋 Thanks for playing! Goodbye.")

# Run the game
main()
