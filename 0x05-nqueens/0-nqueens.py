#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

solutions = []
n = 0
pos = None


def get_input():
    """Retrieves input from user and validates it.

    Returns:
        n (int): The number of queens.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    # Check if the queens are in the same diagonal
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checks if the given group is already in the solutions list.

    Args:
        group (list): A list of tuples, representing the positions of the
        queens.

    Returns:
        bool: True if it exists, otherwise False.
    """
    # global variable to access the solutions list
    global solutions

    # Loop through all the solutions in the solutions list
    for stn in solutions:
        # Counter to check the number of matching positions
        i = 0
        # Loop through all positions in the current solution
        for stn_pos in stn:
            # Loop through all positions in the given group
            for grp_pos in group:
                # If a match is found, increment the counter
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        # If the number of matching positions is equal to the board size,
        # the group is already in the solutions list
        if i == n:
            return True
    # If no match is found, the group is not in the solutions list
    return False


def build_solution(row, group):
    """Recursively build the solutions by adding queens to the board.

    Args:
        row (int): The current row on the chessboard.
        group (list): A list of tuples, representing the positions of queens.

    Returns:
        None: The function modifies the global solutions list.
    """
    # Access the global solutions and n variables
    global solutions
    global n
    # Base case: if all rows have been processed, the solution is complete
    if row == n:
        # Create a copy of the current solution
        tmp0 = group.copy()
        # Check if the solution already exists in the solutions list
        if not group_exists(tmp0):
            # If not, add the solution to the solutions list
            solutions.append(tmp0)
    # Recursive case: if the solution is not complete, keep building it
    else:
        # Loop through each column in the current row
        for col in range(n):
            # Calculate the position index
            a = (row * n) + col
            # Zip the position at the index with the current solution group
            matches = zip(list([pos[a]]) * len(group), group)
            # Check if any of the positions in the current solution group are
            # attacking the position at the index
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            # If there is no attacking queen, add the position to the current
            # solution group
            group.append(pos[a].copy())
            # Check if any of the positions in the current solution group are
            # attacking
            if not any(used_positions):
                # If not, move on to the next row & keep building the solution
                build_solution(row + 1, group)
            # Remove the queen from the group before trying the next column
            group.pop(len(group) - 1)


def get_solutions():
    """Generates all possible solutions to the N queens problem by building
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()

get_solutions()

for solution in solutions:
    print(solution)
