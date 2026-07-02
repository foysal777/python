board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def print_board():
    print("\n")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("\n")






def check_winner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    


    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
        

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False



current_player = "X"
turns = 0


print("Welcome to Tic Tac Toe!")
while turns < 9:
    
    print_board()
    print(f"Player {current_player}'s turn.")
    
    
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                turns += 1
                if check_winner(current_player):
                    print_board()
                    print(f"Player {current_player} wins!")
                    break
                elif turns == 9:
                    print_board()
                    print("It's a tie!")
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("That position is already taken!")
        else:
            print("Invalid input! Please enter numbers between 0 and 2.")
    except ValueError:
        print("Invalid input! Please enter numbers.")



