def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, path):

    if row == 8:
        return True

    for col in range(8):

        if is_safe(board, row, col):

            board[row][col] = 1
            path.append((row, col))

            if solve(board, row + 1, path):
                return True

            board[row][col] = 0
            path.pop()

    return False


def display(board):
    for row in board:
        print(" ".join("Q" if x else "_" for x in row))
    print()


# Create 8 x 8 board
board = [[0] * 8 for _ in range(8)]
path = []

# Solve
if solve(board, 0, path):

    print("========== 8 QUEENS ==========\n")

    for step in range(8):

        temp = [[0] * 8 for _ in range(8)]

        for r in range(step + 1):
            row, col = path[r]
            temp[row][col] = 1

        print("Step", step + 1)
        display(temp)

    print("========== FINAL ==========")
    display(board)

    print("Path Cost =", len(path))
    print("Total Steps =", len(path))

else:
    print("No solution found.")
