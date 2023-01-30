#!/usr/bin/python3
import sys


def nqueens_solutions(n):
    def init_board():
        board = [[' ' for i in range(n)] for j in range(n)]
        return board

    def xout(board, row, col):
        for i in range(col+1, n):
            board[row][i] = 'x'
        for i in range(col-1, -1, -1):
            board[row][i] = 'x'
        for i in range(row+1, n):
            board[i][col] = 'x'
        for i in range(row-1, -1, -1):
            board[i][col] = 'x'
        i, j = row+1, col+1
        while i < n and j < n:
            board[i][j] = 'x'
            i += 1
            j += 1
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            board[i][j] = 'x'
            i -= 1
            j -= 1
        i, j = row-1, col+1
        while i >= 0 and j < n:
            board[i][j] = 'x'
            i -= 1
            j += 1
        i, j = row+1, col-1
        while i < n and j >= 0:
            board[i][j] = 'x'
            i += 1
            j -= 1

    def recursive_solve(board, row, queens, solutions):
        if queens == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'Q':
                        solution.append([i, j])
            solutions.append(solution)
            return solutions
        for col in range(n):
            if board[row][col] == ' ':
                tmp_board = [row[:] for row in board]
                tmp_board[row][col] = 'Q'
                xout(tmp_board, row, col)
                solutions = recursive_solve(tmp_board, row+1, queens+1, solutions)
        return solutions

    board = init_board()
    solutions = recursive_solve(board, 0, 0, [])
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print('N must be a number')
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = nqueens_solutions(int(sys.argv[1]))
    for sol in solutions:
        print(sol)
