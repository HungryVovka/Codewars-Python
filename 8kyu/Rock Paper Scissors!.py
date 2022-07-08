# -----------------------------------------------------------
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
# 
# Examples(Input1, Input2 --> Output):
# 
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
# -----------------------------------------------------------

def rps(p1, p2):
    cases = ['rock', 'paper', 'scissors']
    if p1 == p2:
        return "Draw!"
    if p1 == cases[0] and p2 == cases[1]:
        return "Player 2 won!"
    if p1 == cases[0] and p2 == cases[2]:
        return "Player 1 won!"
    if p1 == cases[1] and p2 == cases[2]:
        return "Player 2 won!"
    if p1 == cases[1] and p2 == cases[0]:
        return "Player 1 won!"
    if p1 == cases[2] and p2 == cases[0]:
        return "Player 2 won!"
    if p1 == cases[2] and p2 == cases[1]:
        return "Player 1 won!"