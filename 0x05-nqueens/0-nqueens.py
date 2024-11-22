#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    solve(board, 0, n, solutions)

    for solution in solutions:
        print(solution)
        print()


def solve(board, col, n, solutions):
    if col == n:
        solution = [(row, board[row].index(1)) for row in range(n)]
        solutions.append(solution)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, col + 1, n, solutions)
            board[row][col] = 0


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
