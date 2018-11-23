player1 = input ('player 1 :enter your choice Rock, Paper, Scissors ? ')
player2 = input ('player 2 :enter your choice Rock, Paper, Scissors ? ')

beats = {'scissors': 'rock','rock': 'paper','paper': 'scissors',}

def play_game(player1, player2, beats):
    if (player1 == beats[player2]):
        return "Player 1 wins,Congratulations."
    elif (player2 == beats[player1]):
        return "Player 2 wins,Congratulations."

if (player1 == player2):
    print ('Tie')
else:
    print (play_game(player1, player2, beats))
