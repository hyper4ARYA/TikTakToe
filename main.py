import tkinter as tk
import numpy as np
import tkinter.messagebox as messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")

        self.current_player = "X"
        self.board = np.empty((3, 3), dtype=str)
        self.player_scores = {"X": 0, "O": 0}

        self.root.geometry("300x400")
        self.create_board()
        self.create_buttons()
        self.create_scorecard()

    def create_board(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def create_buttons(self):
        restart_button = tk.Button(self.root, text="Restart", width=10, height=2, command=self.restart_game)
        restart_button.grid(row=3, column=0, columnspan=2)

        close_button = tk.Button(self.root, text="Close", width=10, height=2, command=self.close_game)
        close_button.grid(row=3, column=2)

    def create_scorecard(self):
        self.scorecard_label = tk.Label(self.root, text="Score: X: 0 - O: 0", font=("Helvetica", 12))
        self.scorecard_label.grid(row=4, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                self.announce_winner()
            else:
                self.toggle_player()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def announce_winner(self):
        winner = self.current_player
        self.player_scores[winner] += 1
        self.scorecard_label.config(text=f"Score: X: {self.player_scores['X']} - O: {self.player_scores['O']}")
        winner_label = tk.Label(self.root, text=f"Player {winner} wins!", font=("Helvetica", 14))
        winner_label.grid(row=5, columnspan=3)
        self.disable_buttons()
        messagebox.showinfo("Game Over", f"Player {winner} wins!")

        # Automatically restart the game after a brief delay (e.g., 2 seconds)
        self.root.after(2000, self.restart_game)

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def enable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.NORMAL)
                button["text"] = ""

    def restart_game(self):
        self.enable_buttons()
        self.board = np.empty((3, 3), dtype=str)
        self.current_player = "X"
        self.clear_winner_label()

    def clear_winner_label(self):
        winner_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        winner_label.grid(row=5, columnspan=3)

    def close_game(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
