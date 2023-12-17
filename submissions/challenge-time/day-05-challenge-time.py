import random

print("Player vs Computer: Rock Paper Scissor")
print(" ")
player = input("Rock, Paper or Scissor? ").lower()

def computer_picks():
    random_num = random.randint(1, 3)
    if (random_num == 1):
        return "rock"
    elif (random_num == 2):
        return 'paper'
    elif (random_num == 3):
        return "scissor"


computer = computer_picks()

def evaluate(player, computer):
    result = ""
    if (player == computer):
        result = "It's a tie"
    elif (player == "rock" and computer == "paper"):
        result = "Computer wins"
    elif (player == "rock" and computer == "scissor"):
        result = "Player wins"
    elif (player == "paper" and computer == "rock"):
        result = "Player wins"
    elif (player == "paper" and computer == "scissor"):
        result = "Computer wins"
    elif (player == "scissor" and computer == "rock"):
        result = "Computer wins"
    elif (player == "scissor" and computer == "paper"):
        result = "Player wins"
    print(" ")
    print(f"Player picked {player} and Computer picked {computer}. {result}")

evaluate(player, computer)
    




