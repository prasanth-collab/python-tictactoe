import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.window.configure(bg="#2c3e50")
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        
        # Colors
        self.bg_color = "#2c3e50"
        self.button_color = "#34495e"
        self.x_color = "#e74c3c"
        self.o_color = "#3498db"
        self.text_color = "#ecf0f1"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack(pady=20)
        
        # Player turn indicator
        self.turn_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s Turn",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.turn_label.pack(pady=10)
        
        # Game board frame
        board_frame = tk.Frame(self.window, bg=self.bg_color)
        board_frame.pack(pady=20)
        
        # Create buttons for the game board
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text="",
                    font=("Arial", 20, "bold"),
                    width=6,
                    height=3,
                    bg=self.button_color,
                    fg=self.text_color,
                    relief="raised",
                    bd=3,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # Reset button
        reset_button = tk.Button(
            self.window,
            text="New Game",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg=self.text_color,
            relief="raised",
            bd=2,
            command=self.reset_game
        )
        reset_button.pack(pady=20)
        
    def button_click(self, row, col):
        index = row * 3 + col
        
        if self.board[index] == "" and self.game_active:
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                bg=self.x_color if self.current_player == "X" else self.o_color,
                state="disabled"
            )
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_active = False
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.game_active = False
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s Turn")
    
    def check_winner(self):
        # Winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ""):
                # Highlight winning combination
                for index in combo:
                    self.buttons[index].config(bg="#f39c12")
                return True
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        
        for button in self.buttons:
            button.config(
                text="",
                bg=self.button_color,
                state="normal"
            )
        
        self.turn_label.config(text=f"Player {self.current_player}'s Turn")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run() 