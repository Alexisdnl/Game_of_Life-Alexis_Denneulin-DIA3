import tkinter as tk
import time

# Constants
CELL_SIZE = 20  # Size of each cell in pixels
GRID_COLOR = "gray"
LIVE_CELL_COLOR = "black"
DEAD_CELL_COLOR = "white"
SLEEP_TIME = 100  # Milliseconds between generations

def get_neighbors(board, x=0, y=0):
    """
    Counts the number of live neighbors around a given cell.
    """
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == '#':
                count += 1
    return count

def next_generation(board):
    """
    Computes the next generation of the board based on the rules of the game.
    """
    new_board = []
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[0])):
            live_neighbors = get_neighbors(board, i, j)
            if board[i][j] == '#' and (live_neighbors == 2 or live_neighbors == 3):
                new_row.append('#')
            elif board[i][j] == ' ' and live_neighbors == 3:
                new_row.append('#')
            else:
                new_row.append(' ')
        new_board.append(new_row)
    return new_board

class GameOfLifeApp:
    def __init__(self, root, board):
        self.root = root
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.canvas = tk.Canvas(root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg=DEAD_CELL_COLOR)
        self.canvas.pack()
        self.running = True
        self.update_board()

    def draw_board(self):
        """
        Draws the cells on the canvas based on the current state of the board.
        """
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                color = LIVE_CELL_COLOR if self.board[i][j] == '#' else DEAD_CELL_COLOR
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=GRID_COLOR)

    def update_board(self):
        """
        Updates the board and redraws the canvas for each generation.
        """
        if self.running:
            self.draw_board()
            self.board = next_generation(self.board)
            self.root.after(SLEEP_TIME, self.update_board)

def main():
    # Define the initial board
    board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

    root = tk.Tk()
    root.title("Game of Life")
    app = GameOfLifeApp(root, board)
    root.mainloop()

if __name__ == "__main__":
    main()