
import random

print("================================")
print("   ROCK PAPER SCISSORS GAME")
print("================================")

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    player = input(
        "\nChoose rock, paper, scissors "
        "or quit: "
    ).lower().strip()

    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Your choice:", player)
    print("Computer's choice:", computer)

    if player == computer:
        print("Result: It's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("Result: You win!")
        player_score += 1

    else:
        print("Result: Computer wins!")
        computer_score += 1

    print("Your score:", player_score)
    print("Computer score:", computer_score)

print("\n===== FINAL SCORE =====")
print("Your score:", player_score)
print("Computer score:", computer_score)
print("Thank you for playing!")
