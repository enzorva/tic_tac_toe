board = [" "] * 9
x = "x"
o = "o"


def display_grid():
    #board = [str(cell) if cell !=1 else "!" for cell in display_board]
    print(f"""
        1    |2    |3
          {board[0]}  |  {board[1]}  |  {board[2]} 
        _____|_____|_____
        4    |5    |6
          {board[3]}  |  {board[4]}  |  {board[5]} 
        _____|_____|_____
        7    |8    |9
          {board[6]}  |  {board[7]}  |  {board[8]}
             |     |
        """)



def get_play(player):
    while True:
        try:
            play = input(f"Vez jogador {player}: ")
            if play.isdigit() and 1 <= int(play) <= 9:
                return play
            else:
                raise ValueError("Digite um número válido entre 1 e 9")
        except ValueError as e:
            print(e)



def highlight_win(a, b, c):
    if b == a + 1:
        board[a] = "-"
        board[b] = "-"
        board[c] = "-"
    elif b == a + 3:
        board[a] = "|"
        board[b] = "|"
        board[c] = "|"
    elif a == 0 and c == 8:
        board[a] = "\\"
        board[b] = "\\"
        board[c] = "\\"
    elif a == 2 and c == 6:
        board[a] = "/"
        board[b] = "/"
        board[c] = "/"



def check_win_row(player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            global winner
            winner = player
            highlight_win(i, i+1, i+2)
            return True
            
    return False  


def check_win_column(player):

    columns = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

    for col in columns:
        if board[col[0]] == board[col[1]] == board[col[2]] == player:
            global winner
            winner = player
            highlight_win(col[0], col[1], col[2])
            return True 
            
    return False    


def check_win_diagonals(player):

    diagonals = [[0, 4, 8], [2, 4, 6]]

    for dialgonal in diagonals:
        if board[dialgonal[0]] == board[dialgonal[1]] == board[dialgonal[2]] == player:
            global winner
            winner = player
            highlight_win(dialgonal[0], dialgonal[1], dialgonal[2])
            return True
    return False



def check_win(player):
    if check_win_row(player) or check_win_column(player) or check_win_diagonals(player):
        print(f"Jogador {winner} ganhou!!!")
        return True
    return False



         


def game_loop():
    
    for j in range(9):
        player = x if j % 2 == 0 else o

        move = get_play(player)
        quadrant = int(move) - 1
        
        if board[quadrant] == " ":
            board[quadrant] = player
            display_grid()

            if check_win(player):
                display_grid()
                break
                
                
        else:
            print("Quadrante Inválido")

        if j == 8:
            print("Deu véia!!!")




def main():
    display_grid()
    game_loop()

main()