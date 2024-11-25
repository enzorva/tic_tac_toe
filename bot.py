import random
o = "o"
x = "x"

def bot(display_grid,board, j):
    if j == 1:
        choice = random.randrange(9)
        quadrant = int(choice) - 1
        while board[quadrant] != " ":
            choice = random.randrange(9)
            quadrant = int(choice) - 1
        board[quadrant] = o
        display_grid()
    else:
    # Winning Moves
        for i in range(0, 9, 3):  # Check rows
            if board[i] == board[i + 1] == o and board[i + 2] == " ":
                board[i + 2] = o
                display_grid()
                return
            elif board[i + 1] == board[i + 2] == o and board[i] == " ":
                board[i] = o
                display_grid()
                return
            elif board[i] == board[i + 2] == o and board[i + 1] == " ":
                board[i + 1] = o
                display_grid()
                return

        for i in range(3):  # Check columns
            if board[i] == board[i + 3] == o and board[i + 6] == " ":
                board[i + 6] = o
                display_grid()
                return
            elif board[i + 3] == board[i + 6] == o and board[i] == " ":
                board[i] = o
                display_grid()
                return
            elif board[i] == board[i + 6] == o and board[i + 3] == " ":
                board[i + 3] = o
                display_grid()
                return

        # Check diagonals
        diagonals = [(0, 4, 8), (2, 4, 6)]
        for d in diagonals:
            if board[d[0]] == board[d[1]] == o and board[d[2]] == " ":
                board[d[2]] = o
                display_grid()
                return
            elif board[d[1]] == board[d[2]] == o and board[d[0]] == " ":
                board[d[0]] = o
                display_grid()
                return
            elif board[d[0]] == board[d[2]] == o and board[d[1]] == " ":
                board[d[1]] = o
                display_grid()
                return

        # Blocking Moves
        for i in range(0, 9, 3):  # Check rows
            if board[i] == board[i + 1] == x and board[i + 2] == " ":
                board[i + 2] = o
                display_grid()
                return
            elif board[i + 1] == board[i + 2] == x and board[i] == " ":
                board[i] = o
                display_grid()
                return
            elif board[i] == board[i + 2] == x and board[i + 1] == " ":
                board[i + 1] = o
                display_grid()
                return

        for i in range(3):  # Check columns
            if board[i] == board[i + 3] == x and board[i + 6] == " ":
                board[i + 6] = o
                display_grid()
                return
            elif board[i + 3] == board[i + 6] == x and board[i] == " ":
                board[i] = o
                display_grid()
                return
            elif board[i] == board[i + 6] == x and board[i + 3] == " ":
                board[i + 3] = o
                display_grid()
                return

        # Check diagonals
        for d in diagonals:
            if board[d[0]] == board[d[1]] == x and board[d[2]] == " ":
                board[d[2]] = o
                display_grid()
                return
            elif board[d[1]] == board[d[2]] == x and board[d[0]] == " ":
                board[d[0]] = o
                display_grid()
                return
            elif board[d[0]] == board[d[2]] == x and board[d[1]] == " ":
                board[d[1]] = o
                display_grid()
                return

        # Strategic Moves (fallback)
        if board[4] == " ":  # Center
            board[4] = o
            display_grid()
            return

        for corner in [0, 2, 6, 8]:  # Corners
            if board[corner] == " ":
                board[corner] = o
                display_grid()
                return

        for edge in [1, 3, 5, 7]:  # Edges
            if board[edge] == " ":
                board[edge] = o
                display_grid()
                return
