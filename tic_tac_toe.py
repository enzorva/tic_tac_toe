from bot import Bot

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.x = "x"
        self.o = "o"

    def display_grid(self):
        print(f"""
            1    |2    |3
              {self.board[0]}  |  {self.board[1]}  |  {self.board[2]} 
            _____|_____|_____
            4    |5    |6
              {self.board[3]}  |  {self.board[4]}  |  {self.board[5]} 
            _____|_____|_____
            7    |8    |9
              {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}
                 |     |
            """)

    def highlight_win(self, a, b, c):
        if b == a + 1:
            self.board[a], self.board[b], self.board[c] = "-", "-", "-"
        elif b == a + 3:
            self.board[a], self.board[b], self.board[c] = "|", "|", "|"
        elif a == 0 and c == 8:
            self.board[a], self.board[b], self.board[c] = "\\", "\\", "\\"
        elif a == 2 and c == 6:
            self.board[a], self.board[b], self.board[c] = "/", "/", "/"



    def check_win_row(self, player):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                self.highlight_win(i, i+1, i+2)
                return True
                
        return False  


    def check_win_column(self, player):
        columns = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        for col in columns:
            if self.board[col[0]] == self.board[col[1]] == self.board[col[2]] == player:
                self.highlight_win(col[0], col[1], col[2])
                return True 
        return False    


    def check_win_diagonals(self, player):
        diagonals = [[0, 4, 8], [2, 4, 6]]
        for dialgonal in diagonals:
            if self.board[dialgonal[0]] == self.board[dialgonal[1]] == self.board[dialgonal[2]] == player:
                self.highlight_win(dialgonal[0], dialgonal[1], dialgonal[2])
                return True
        return False



    def check_win(self, player):
        if self.check_win_row(player) or self.check_win_column(player) or self.check_win_diagonals(player):
            print(f"Jogador {player} ganhou!!!")
            return True
        return False

        
class GameController:
    def __init__(self):
        self.game = TicTacToe()
        self.adversary = Bot()

    def get_play(self, player):
        while True:
            try:
                play = input(f"Vez jogador {player}: ")
                if play.isdigit() and 1 <= int(play) <= 9:
                    return play
                else:
                    raise ValueError("Digite um número válido entre 1 e 9")
            except ValueError as e:
                print(e)

    def game_loop(self, game_mode, difficulty):
        for j in range(9):
            if game_mode == "bot":
                if j % 2 == 0:
                    player = self.game.x
                    move = self.get_play(player)
                    quadrant = int(move) - 1 
                    if self.game.board[quadrant] == " ":
                        self.game.board[quadrant] = player
                        self.game.display_grid()
                        if self.game.check_win(player):
                            self.game.display_grid()
                            break        
                    else:
                        print("Quadrante Inválido")
                    if j == 8:
                        print("Deu véia!!!")
                else:
                    print("Vez jogador o...")
                    match difficulty:
                        case "1":
                            self.adversary.easy_bot(self.game.display_grid, self.game.board)
                        case "2":
                            self.adversary.medium_bot(self.game.display_grid, self.game.board, j)
                        case "3":
                            self.adversary.hard_bot(self.game.display_grid, self.game.board)
                    player = self.game.o
                    if self.game.check_win(player):
                        self.game.display_grid()
                        break
                    if j == 8:
                        print("Deu véia!!!")
            elif game_mode == "player2":
                player = self.game.x if j % 2 == 0 else self.game.o
                move = self.get_play(player)
                quadrant = int(move) - 1
                if self.game.board[quadrant] == " ":
                    self.game.board[quadrant] = player
                    self.game.display_grid()
                    if self.game.check_win(player):
                        self.game.display_grid()
                        break     
                else:
                    print("Quadrante Inválido")
                if j == 8:
                    print("Deu véia!!!")
            else:
                raise ValueError("Comando invalido, digite bot ou player2")


def main():
    controller = GameController()

    game_mode = input("Escolha modo de jogo (bot ou player2): ")
    while game_mode != "bot" and game_mode != "player2":
        game_mode = input("Escolha modo de jogo (bot ou player2): ")

    if game_mode == "bot":
        valid_difficulties = ["1", "2", "3", "4"]
        difficulty = None
        while difficulty not in valid_difficulties:
            difficulty =  input("""Escolha a dificuldade:
        1. Easy
        2. Medium
        3. Hard
        4. Hardcore\n""")
            
    controller.game.display_grid()
    controller.game_loop(game_mode, difficulty)

main()