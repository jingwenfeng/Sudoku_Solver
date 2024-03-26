class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.subgrid_size = 3

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    def find_empty_location(self):
        for i in range(self.size):
            for j in range(self.size):
                try:
                    if self.board[i][j] == 0:
                        return i, j
                except IndexError:
                    print(f"Error: Invalid board dimensions at position ({i}, {j})")
                    return None
        return None

    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False

        if num in (self.board[i][col] for i in range(self.size)):
            return False

        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        empty_loc = self.find_empty_location()
        if not empty_loc:
            return True
        row, col = empty_loc

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False