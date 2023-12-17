print("Rock, Paper or Scissors")
player_1 = input("Player1: ").lower()
player_2 = input("Player2: ").lower()


if (player_1 == 'rock' and player_2 == 'rock'):
    print("It's a tie")
elif (player_1 == 'rock' and player_2 == 'paper'):
    print("Player2 Wins!")
elif (player_1 == 'rock' and player_2 == 'scissors'):
    print("Player1 Wins!")
elif (player_1 == 'paper' and player_2 == 'rock'):
    print("Player1 Wins!")
elif (player_1 == 'paper' and player_2 == 'paper'):
    print("It's a tie")
elif (player_1 == 'paper' and player_2 == 'scissors'):
    print("Player2 Wins!")
elif (player_1 == 'scissors' and player_2 == 'rock'):
    print("Player2 Wins!")
elif (player_1 == 'scissors' and player_2 == 'paper'):
    print("Player1 Wins!")
elif (player_1 == 'scissors' and player_2 == 'scissors'):
    print("It's a tie!")
else:
    print("Something went wrong, please try again.")