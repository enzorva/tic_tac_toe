from bot import Bot
import time
import threading
import sys

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
            print(f"{player} wins!!!")
            return True
        return False

        
class GameController:
    def __init__(self):
        self.game = TicTacToe()
        self.adversary = Bot()
        self.timer_active = True

    def get_play(self, player):
        while True:
            try:
                play = input(f"{player}'s turn: ")
                if play.isdigit() and 1 <= int(play) <= 9:
                    return play
                else:
                    raise ValueError("Type a number between 1 to 9")
            except ValueError as e:
                print(e)


    def countdown_timer(self, duration):
        """Countdown timer that updates on a separate line."""
        sys.stdout.write("\033[s")  # Save the current cursor position
        while duration > 0 and self.timer_active:
            sys.stdout.write("\033[u")  # Restore the saved cursor position
            sys.stdout.write(f"\033[KTime remaining: {duration} seconds\n")  # Clear line and print timer
            sys.stdout.flush()
            time.sleep(1)
            duration -= 1
        if duration == 0:
            self.timer_active = False
            sys.stdout.write("\033[u\033[KTime's up! Game over.\n")  # Notify when time is up
            sys.stdout.flush()

    def game_loop(self, game_style, difficulty):
        for j in range(9):
            if game_style == "bot":
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
                        print("Invalid Quadrant")
                    if j == 8:
                        print("Draw!!!")
                else:
                    print("o's turn...")
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
                        print("Draw!!!")
            elif game_style == "player2":
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
                    print("Invalid Quadrant")
                if j == 8:
                    print("Draw!!!")
            else:
                raise ValueError("Invalid command, type bot or player2")
            

            
    def game_timed_loop(self, game_style, difficulty):
        timer_thread = threading.Thread(target= self.countdown_timer, args=(20,))
        timer_thread.start()
        for j in range(9):
            if game_style == "bot":
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
                        print("Invalid Quadrant")
                    if j == 8:
                        print("Draw!!!")
                else:
                    print("o's turn...")
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
                        print("Draw!!!")
            elif game_style == "player2":
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
                    print("Invalid Quadrant")
                if j == 8:
                    print("Draw!!!")
            else:
                raise ValueError("Invalid command, type bot or player2")
        else:
            print("Time is over")
        self.timer_active = False  # Ensure timer stops after the game ends
        timer_thread.join() 
            


def main():
    controller = GameController()

    game_mode = input("""Choose game mode: 
    1. With countdown timer
    2. Without countdown timer\n""")
    while game_mode != "1" and game_mode != "2":
        game_mode = input("""Choose game mode: 
    1. With countdown timer
    2. Without countdown timer\n""")
        
    if game_mode == "2":

        game_style = input("Choose game style (bot or player2): ")
        while game_style != "bot" and game_style != "player2":
            game_style = input("Choose game style (bot or player2): ")

        if game_style == "bot":
            valid_difficulties = ["1", "2", "3", "4"]
            difficulty = None
            while difficulty not in valid_difficulties:
                difficulty =  input("""Choose difficulty:
            1. Easy
            2. Medium
            3. Hard
            4. Hardcore\n""")
                
        controller.game.display_grid()
        controller.game_loop(game_style, difficulty)

    else:
        game_style = input("Choose game style (bot or player2): ")
        while game_style != "bot" and game_style != "player2":
            game_style = input("Choose game style (bot or player2): ")

        if game_style == "bot":
            valid_difficulties = ["1", "2", "3", "4"]
            difficulty = None
            while difficulty not in valid_difficulties:
                difficulty =  input("""Choose difficulty:
            1. Easy
            2. Medium
            3. Hard
            4. Hardcore\n""")
                
        controller.game.display_grid()
        controller.game_timed_loop(game_style, difficulty)

main()