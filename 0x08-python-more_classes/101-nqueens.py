#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for i in range(n)] for j in range(n)]
    return board


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = [[r, c] for r in range(len(board))
    for c in range(len(board)) if board[r][c] == "Q"]
    return solution


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    for i in range(len(board)):
        board[row][i] = "x"
        board[i][col] = "x"
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        board[r][c] = "x"
    for r, c in zip(range(row+1, len(board)), range(col+1, len(board))):
        board[r][c] = "x"
    for r, c in zip(range(row-1, -1, -1), range(col+1, len(board))):
        board[r][c] = "x"
    for r, c in zip(range(row+1, len(board)), range(col-1, -1, -1)):
        board[r][c] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = [row[:] for row in board]
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
