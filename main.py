# TODO
#   1.  Create input for x or o
#   1.5 get ascii of tic tac toe
#   2.  Pass input into if "query" to determine inpout and resulting into output print of tic tak toe
#   3.  while loop
import os
MARK_SPOT = {"a1": "-",
             "a2": "-",
             "a3": "-",
             "b1": "-",
             "b2": "-",
             "b3": "-",
             "c1": "-",
             "c2": "-",
             "c3": "-"}


def tictactoe_board(spot):
    tictactoe = f"""\n           a     b     c
              |     |
        1  {spot["a1"]}  |  {spot["b1"]}  |  {spot["c1"]}
         _____|_____|_____
              |     |
        2  {spot["a2"]}  |  {spot["b2"]}  |  {spot["c2"]}
         _____|_____|_____
              |     |
        3  {spot["a3"]}  |  {spot["b3"]}  |  {spot["c3"]}
              |     |     \n"""
    return tictactoe


def winner(spot):
    # Player 1 wins
    if spot["a1"] == "o" and spot["a2"] == "o" and spot["a3"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["b1"] == "o" and spot["b2"] == "o" and spot["b3"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["c1"] == "o" and spot["c2"] == "o" and spot["c3"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["c1"] == "o" and spot["c2"] == "o" and spot["c3"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["a1"] == "o" and spot["b1"] == "o" and spot["c1"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["a2"] == "o" and spot["b2"] == "o" and spot["c2"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["a3"] == "o" and spot["b3"] == "o" and spot["c3"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["a1"] == "o" and spot["b2"] == "o" and spot["c3"] == "o":
        print("Player 1 wins!")
        return False
    elif spot["a3"] == "o" and spot["b2"] == "o" and spot["c1"] == "o":
        print("Player 1 wins!")
        return False

    # Player 2 wins
    if spot["a1"] == "x" and spot["a2"] == "x" and spot["a3"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["b1"] == "x" and spot["b2"] == "x" and spot["b3"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["c1"] == "x" and spot["c2"] == "x" and spot["c3"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["c1"] == "x" and spot["c2"] == "x" and spot["c3"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["a1"] == "x" and spot["b1"] == "x" and spot["c1"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["a2"] == "x" and spot["b2"] == "x" and spot["c2"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["a3"] == "x" and spot["b3"] == "x" and spot["c3"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["a1"] == "x" and spot["b2"] == "x" and spot["c3"] == "x":
        print("Player 1 wins!")
        return False
    elif spot["a3"] == "x" and spot["b2"] == "x" and spot["c1"] == "x":
        print("Player 1 wins!")
        return False

    # Tie
    elif "-" not in spot.values():
        print("Games ends in a tie!")
        return False

    else:
        return True


board = tictactoe_board(MARK_SPOT)
print(f"Welcome to the Tic Tak Toe - Game!\n"
      "This is a two player game, here is the board:"
      f"\n{board}")

run = True
# while loop that runs the game till it ends!
while run:
    player_one_turn = True
    # while loop for player 1
    while player_one_turn:
        player_one = input("Player 1 your mark is o! \nChoose a spot, e.g. b2 for the center: ")
        if player_one in MARK_SPOT.keys() and MARK_SPOT[player_one] == "-":
            MARK_SPOT[player_one] = "o"
            player_one_turn = False
        elif MARK_SPOT[player_one] == "x":
            print("Player 2 has already placed his mark there! Try again.")
        else:
            print("Wrong input, try again!\n")

    updated_board = tictactoe_board(MARK_SPOT)
    print(updated_board)
    run = winner(MARK_SPOT)

    player_two_turn = True
    # while loop for player 2
    while player_two_turn and run:
        player_two = input("Player 2 your mark is x! \nChoose a spot, e.g. b2 for the center: ")
        if player_two in MARK_SPOT.keys() and MARK_SPOT[player_two] == "-":
            MARK_SPOT[player_two] = "x"
            player_two_turn = False
        elif MARK_SPOT[player_two] == "o":
            print("Player 1 has already placed his mark there! Try again.")
        else:
            print("Wrong input, try again!\n")

    updated_board = tictactoe_board(MARK_SPOT)
    print(updated_board)

    run = winner(MARK_SPOT)

    # Game ends. Start a new one?
    if not run:
        again = input("Want to play again? Y/N: ").lower()
        if again == "y":
            os.system('cls')
            run = True
