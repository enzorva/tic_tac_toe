board = [" "] * 9
x = "x"
o = "o"


def display_grid():
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



def check_win():
    #linhas
    if board[0] in [x, o] and all(i == board[0] for i in board[:3]):
        print(f"Jogador {board[0]} ganhou")
        return True
    elif board[3] in [x, o] and all(i == board[3] for i in board[3:6]):
        print(f"Jogador {board[0]} ganhou")
        return True
    elif board[6] in [x, o] and all(i == board[6] for i in board[6:9]):
        print(f"Jogador {board[0]} ganhou")
        return True
    
    #colunas para x
    elif board[0] == x and board[3] == x and board[6] == x:
        print("Jogador x ganhou")
        return True
    elif board[1] == x and board[4] == x and board[7] == x:
        print("Jogador x ganhou")
        return True
    elif board[2] == x and board[5] == x and board[8] == x:
        print("Jogador x ganhou")
        return True

    #colunas para o
    elif board[0] == o and board[3] == o and board[6] == o:
        print("Jogador o ganhou")
        return True
    elif board[1] == o and board[4] == o and board[7] == o:
        print("Jogador o ganhou")
        return True
    elif board[2] == o and board[5] == o and board[8] == o:
        print("Jogador o ganhou")
        return True

    #diagonais para x
    elif board[0] == x and board[4] == x and board[8] == x:
        print("Jogador x ganhou")
        return True
    elif board[2] == x and board[4] == x and board[6] == x:
        print("Jogador x ganhou")
        return True
    
    #diagonais para o
    elif board[0] == o and board[4] == o and board[8] == o:
        print("Jogador o ganhou")
        return True
    elif board[2] == o and board[4] == o and board[6] == o:
        print("Jogador o ganhou")
        return True



def game_loop():
    
    for j in range(9):
        if check_win():
            break
        player = x if j % 2 == 0 else o
        move = get_play(player)
        quadrant = int(move) - 1
        if board[quadrant] == " ":
            if player == x:
                board[quadrant] = x
                display_grid() 
            else:
                board[quadrant] = o
                display_grid() 
        else:
            print("Quadrante Inválido")



def main():
    display_grid()
    game_loop()

main()