# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way 
# that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain
# all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents
# a valid Sudoku puzzle according to the layout rules described above.
# Note that the puzzle represented by grid does not have to be solvable.


import collections


def solution(board):

    cols = collections.defaultdict(set)  # hashset for the columns visited
    rows = collections.defaultdict(set)  # hashset for the rows visited
    squares = collections.defaultdict(set)  # hashset for the  3x3 sqaure

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True


grid = [
    [".", ".", ".", "1", "4", ".", ".", "2", "."],
    [".", ".", "6", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", ".", ".", ".", "."],
    [".", "6", "7", ".", ".", ".", ".", ".", "9"],
    [".", ".", ".", ".", ".", ".", "8", "1", "."],
    [".", "3", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", "7", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", "7", "."],
]

print(solution(grid))
