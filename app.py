import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()
    
# Create a new Player called played starting at position 3,2
player = player.Player(3, 2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    if selection == 'w':
        player.moveUp()
        print(board.checkMove)
    elif selection == 's':
        player.moveDown()
        print(board.checkMove)
    elif selection == 'a':
        player.moveLeft()
        print(board.checkMove)
    elif selection == 'd':
        player.moveRight()
        print(board.checkMove)
    else:
        print("Not a selection")

    # Check if the player has won, if so print a message and break the loop!
    if board.checkWin(player.rowPosition, player.columnPosition):
        print("You won!")
        break