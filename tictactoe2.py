import tkinter as tk
import numpy as np

# Define the player symbols
player_x = "X"
player_o = "O"
current_player = player_x

# Initialize the board as a 2D list
board = [[0, 0, 0] for _ in range(3)]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

def set_tile(row, column):
    global current_player
    # Check if the button has already been clicked
    if board[row][column] == 0:
        # Update the board with the current player's symbol
        board[row][column] = current_player
        buttons[row][column].config(text=current_player)
        # Disable the button after it's clicked
        buttons[row][column].config(state=tk.DISABLED)
        
        # Check if the current player has won
        if check_winner(current_player):
            label.config(text=f"{current_player} wins!")
            disable_all_buttons()
        elif all(buttons[r][c].cget('state') == tk.DISABLED for r in range(3) for c in range(3)):
            label.config(text="It's a draw!")
        else:
            # Switch players
            current_player = player_o if current_player == player_x else player_x
            label.config(text=f"{current_player}'s turn")

def check_winner(player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def disable_all_buttons():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state=tk.DISABLED)

# Set up the window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=f"{current_player}'s turn", font=("Consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3)

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for column in range(3):
        button = tk.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_gray, foreground=color_blue, width=4, height=1,
                           command=lambda r=row, c=column: set_tile(r, c))
        button.grid(row=row+1, column=column)
        button_row.append(button)
    buttons.append(button_row)

frame.pack()
window.mainloop()
