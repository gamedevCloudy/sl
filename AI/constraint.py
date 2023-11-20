from graph import Graph

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def solve_n_queens_backtracking(board, col, n):
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_backtracking(board, col + 1, n) or res
            board[i][col] = 0  # Backtrack

    return res

def solve_n_queens_branch_and_bound(board, col, n, min_conflicts):
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n) and min_conflicts[i][col] == 0:
            board[i][col] = 1
            update_conflicts(min_conflicts, i, col, n, 1)
            res = solve_n_queens_branch_and_bound(board, col + 1, n, min_conflicts) or res
            board[i][col] = 0  # Backtrack
            update_conflicts(min_conflicts, i, col, n, -1)

    return res

def update_conflicts(min_conflicts, row, col, n, value):
    for i in range(n):
        min_conflicts[row][i] += value
        min_conflicts[i][col] += value

    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        min_conflicts[i][j] += value

    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        min_conflicts[i][j] += value

# Example usage for Backtracking:
n = 8  # Change this to the desired size of the chessboard
board_backtracking = [[0] * n for _ in range(n)]
solve_n_queens_backtracking(board_backtracking, 0, n)

# Example usage for Branch and Bound:
n = 8  # Change this to the desired size of the chessboard
board_branch_and_bound = [[0] * n for _ in range(n)]
min_conflicts = [[0] * n for _ in range(n)]
solve_n_queens_branch_and_bound(board_branch_and_bound, 0, n, min_conflicts)
