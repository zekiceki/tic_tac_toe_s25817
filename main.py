import tkinter as tk

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.players = []
        self.grid_size = 0
        self.player_symbols = {}
        self.current_player_index = 0
        self.board = []

        self.initialize_game()

    def initialize_game(self):
        num_players = int(input("Enter the number of players (2 to 4): "))
        self.get_player_names(num_players)
        self.get_grid_size()
        self.assign_player_symbols()
        self.create_board()

    def get_player_names(self, num_players):
        for i in range(num_players):
            name = input(f"Enter name for Player {i + 1}: ")
            self.players.append(name)

    def get_grid_size(self):
        self.grid_size = int(input("Enter the size of the game grid (5 to 25): "))

    def assign_player_symbols(self):
        for player in self.players:
            symbol = input(f"Enter symbol for {player}: ")
            self.player_symbols[player] = symbol

    def create_board(self):
        self.buttons = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.board = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = tk.Button(self.root, text="", width=4, height=2, command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            current_player = self.players[self.current_player_index]
            symbol = self.player_symbols[current_player]
            self.board[row][col] = symbol
            self.buttons[row][col].config(text=symbol)

            if self.check_winner():
                winner = self.players[self.current_player_index]
                print(f"{winner} wins!")
                self.root.quit()
            elif all(cell != ' ' for row in self.board for cell in row):
                print("It's a draw!")
                self.root.quit()
            else:
                self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def check_winner(self):

        for row in self.board:
            if all(cell == row[0] and cell != ' ' for cell in row):
                return True


        for col in range(self.grid_size):
            if all(row[col] == self.board[0][col] and self.board[0][col] != ' ' for row in self.board):
                return True


        if all(self.board[i][i] == self.board[0][0] and self.board[0][0] != ' ' for i in range(self.grid_size)):
            return True
        if all(self.board[i][self.grid_size - i - 1] == self.board[0][self.grid_size - 1] and self.board[0][self.grid_size - 1] != ' ' for i in range(self.grid_size)):
            return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
