import tkinter as tk

def set_tile(row, column):
    global curr_player, game_over
    if game_over or board[row][column]["text"] != "":
        return
    board[row][column]["text"] = curr_player
    if curr_player == playerO:  # Switch player
        curr_player = playerX
    else:
        curr_player = playerO
    label["text"] = curr_player + "'s Turn"
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_lightgrey)
            game_over = True
            return
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_lightgrey)
            game_over = True
            return
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_lightgrey)
        game_over = True
        return
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_lightgrey)
        board[1][1].config(foreground=color_yellow, background=color_lightgrey)
        board[2][0].config(foreground=color_yellow, background=color_lightgrey)
        game_over = True
        return
    if turns == 9:
        game_over = True
        label.config(text="Tie", foreground=color_yellow, background=color_lightgrey)

def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=curr_player + "'s Turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_lightgrey = "#646464"

turns = 0
game_over = False

window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player + "'s Turn", font=("consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

button_size = 50
for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("consolas", button_size, "bold"),
                                       background=color_gray, foreground=color_blue, width=4, height=1,
                                       command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tk.Button(frame, text="Restart", font=("consolas", 20), background=color_gray, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

def adjust_window_size(event):
    width = event.width
    height = event.height
    new_button_size = min(width, height) // 10
    for row in range(3):
        for column in range(3):
            board[row][column].config(font=("consolas", new_button_size, "bold"))

window.bind("<Configure>", adjust_window_size)
window.mainloop()
