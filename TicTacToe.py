from tkinter import *
import tkinter.messagebox

screen = Tk()
screen.title("Tic Tac Toe")
screen.configure(bg="BLACK")
screen.iconbitmap('tictactoe_icon.ico')

row1 = []
row2 = []
row3 = []
ll = [row1, row2, row3]
player = 'X'
clicks = 0
frames = []
cell_width = 25
cell_length = 25

for frame in range(4):
    frames.append(Frame(screen, bg="BLACK"))
    frames[frame].pack(side=TOP)


def checkWinner():
    for t in range(len(ll)):
        # row check
        if ll[t][0]["text"] == ll[t][1]["text"] == ll[t][2]["text"] and ll[t][0]["text"] != '   ':
            return ll[t][0]["text"]

        # column check
        if ll[0][t]["text"] == ll[1][t]["text"] == ll[2][t]["text"] and ll[0][t]["text"] != '   ':
            return ll[0][t]["text"]
        # Diagonal check
    if ll[0][0]["text"] == ll[1][1]["text"] == ll[2][2]["text"] and ll[0][0]["text"] != '   ':
        return ll[0][0]["text"]
    if ll[0][2]["text"] == ll[1][1]["text"] == ll[2][0]["text"] and ll[0][2]["text"] != '   ':
        return ll[0][2]["text"]
    return None


def RestartBtn():
    global player, clicks
    clicks = 0
    player = 'X'
    display_label.config(text="Player X")
    for restart in range(3):
        for h in range(3):
            ll[restart][h]["state"] = NORMAL
            ll[restart][h].config(text='   ', font=("Arial", 28, "bold"))


def BtnClick(row, cell):
    global player, clicks
    clicks += 1

    ll[row][cell].configure(text=player, font=("Arial", 30, "bold"))
    ll[row][cell]["state"] = DISABLED

    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    winner = checkWinner()
    if winner:
        print(f"Player {winner} Wins")
        message = tkinter.messagebox.askyesno("Tic Tac Toe", f"Winner is Player {winner}\nDo you want to play again?")
        if message:
            RestartBtn()
        else:
            quit(1)

    if clicks == 9:
        print("Draw!")
        messageDraw = tkinter.messagebox.askyesno("Tic Tac Toe", "Draw!\nDo you want to retry?")
        if messageDraw:
            RestartBtn()
        if not messageDraw:
            quit(1)

    display_label.config(text=f"Player {player}")


for i in range(3):
    for j in range(3):
        ll[i].append(Button(frames[i], relief="ridge", text='   ', font=("Arial", 28, "bold"),
                            command=lambda d=i, c=j: BtnClick(d, c)))
        ll[i][j].pack(side=LEFT, fill=BOTH, pady=15, padx=15)

res = Button(frames[3], text='Restart', command=lambda: RestartBtn(), font=("Arial", 20, "bold"))
res.pack(side=LEFT, ipadx=cell_length, ipady=cell_width, pady=15, padx=15, anchor=N)

display_label = Label(frames[3], text="Player X", font=("Arial", 23, "bold"), relief="raised")
display_label.pack(side=RIGHT, ipadx=cell_length, ipady=cell_width + 6, pady=15, padx=15, anchor=N)

screen.mainloop()
