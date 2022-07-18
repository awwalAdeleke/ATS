import sys


class TicTacToe:

    def __init__(self,player) -> None:
        self.a_1 = 0
        self.b_1 = 0
        self.c_1 = 0
        self.a_2 = 0
        self.b_2 = 0
        self.c_2 = 0
        self.a_3 = 0
        self.b_3 = 0
        self.c_3 = 0
        self.player = player.upper()

        self.board = [[self.a_1, self.a_2, self.a_3],
                      [self.b_1, self.b_2, self.b_3],
                      [self.c_1, self.c_2, self.c_3]]

        self.combo = []

        if self.player == "X":
            self.x_play()
        elif self.player == "O":
            self.o_play()

    def x_play(self):

        vertical = int(input(f"Player {self.player}, which position are we playing? 1 for Top, 2 for Middle, 3 for Bottom: "))
        horizontal = int(input(f"Player {self.player}, which position are we playing? 1 for Left, 2 for Middle, 3 for Right: "))

        if vertical == 1 and horizontal == 1:
            if self.a_1 == 0:
                self.a_1 = "X"
            print(self.check_play())
            self.combo.append(self.a_1)
            self.o_play()
        elif vertical == 1 and horizontal == 2:
            if self.a_2 == 0:
                self.a_2 = "X"
            print(self.check_play())
            self.combo.append(self.a_2)
            self.o_play()
        elif vertical == 1 and horizontal == 3:
            if self.a_3 == 0:
                self.a_3 = "X"
            print(self.check_play())
            self.combo.append(self.a_3)
            self.o_play()
        elif vertical == 2 and horizontal == 1:
            if self.b_1 == 0:
                self.b_1 = "X"
            print(self.check_play())
            self.combo.append(self.b_1)
            self.o_play()
        elif vertical == 2 and horizontal == 2:
            if self.b_2 == 0:
                self.b_2 = "X"
            print(self.check_play())
            self.combo.append(self.b_2)
            self.o_play()
        elif vertical == 2 and horizontal == 3:
            if self.b_3 == 0:
                self.b_3 = "X"
            print(self.check_play())
            self.win()
            self.o_play()
        elif vertical == 3 and horizontal == 1:
            if self.c_1 == 0:
                self.c_1 = "X"
            print(self.check_play())
            self.win()
            self.o_play()
        elif vertical == 3 and horizontal == 2:
            if self.c_2 == 0:
                self.c_2 = "X"
            print(self.check_play())
            self.win()
            self.o_play()
        elif vertical == 3 and horizontal == 3:
            if self.c_3 == 0:
                self.c_3 = "X"
            print(self.check_play())
            self.win()
            self.o_play()

    def o_play(self):

        vertical = int(input(f"Player {self.player}, which position are we playing? 1 for Top, 2 for Middle, 3 for Bottom: "))
        horizontal = int(input(f"Player {self.player}, which position are we playing? 1 for Left, 2 for Middle, 3 for Right: "))

        if vertical == 1 and horizontal == 1:
            if self.a_1 == 0:
                self.a_1 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 1 and horizontal == 2:
            if self.a_2 == 0:
                self.a_2 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 1 and horizontal == 3:
            if self.a_3 == 0:
                self.a_3 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 2 and horizontal == 1:
            if self.b_1 == 0:
                self.b_1 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 2 and horizontal == 2:
            if self.b_2 == 0:
                self.b_2 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 2 and horizontal == 3:
            if self.b_3 == 0:
                self.b_3 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 3 and horizontal == 1:
            if self.c_1 == 0:
                self.c_1 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 3 and horizontal == 2:
            if self.c_2 == 0:
                self.c_2 = "O"
            print(self.check_play())
            self.win()
            self.x_play()
        elif vertical == 3 and horizontal == 3:
            if self.c_3 == 0:
                self.c_3 = "O"
            print(self.check_play())
            self.win()
            self.x_play()




    def check_play(self):
        return f"\n\t\t {self.a_1} | {self.a_2} | {self.a_3} \n\
                ——— ——— ———\n\
                 {self.b_1} | {self.b_2} | {self.b_3} \n\
                ——— ——— ———\n\
                 {self.c_1} | {self.c_2} | {self.c_3} \n\
                      "

    def win(self):
        if (self.a_1 == self.a_2 == self.a_3) == "X" or (self.a_1 == self.a_2 == self.a_3) == "O": # First horizontal
            return "You have won!"
        if (self.b_1 == self.b_2 == self.b_3) == "X" or (self.b_1 == self.b_2 == self.b_3) == "O": # Second horizontal
            return "You have won!"
        if (self.c_1 == self.c_2 == self.c_3) == "X" or (self.c_1 == self.c_2 == self.c_3) == "O": # Third horizontal
            return "You have won!"
        if (self.a_1 == self.b_1 == self.c_1) == "X" or (self.a_1 == self.b_1 == self.c_1) == "O": # First vertical
            return "You have won!"
        if (self.a_2 == self.b_2 == self.c_2) == "X" or (self.a_2 == self.b_2 == self.c_2) == "O": # Second vertical
            return "You have won!"
        if (self.a_3 == self.b_3 == self.c_3) == "X" or (self.a_3 == self.b_3 == self.c_3) == "O": # Third vertical
            return "You have won!"
        if (self.a_1 == self.b_2 == self.c_3) == "X" or (self.a_1 == self.b_2 == self.c_3) == "O": # Upper left to Lower right
            return "You have won!"
        if (self.a_3 == self.b_2 == self.c_1) == "X" or (self.a_3 == self.b_2 == self.c_1) == "O": # Upper right to Lower left
            return "You have won!"
        return



if __name__ == '__main__':
    start = input("Who is starting the game: ").upper()
    if start == "X":
        game1 = TicTacToe("X")
    elif start == "O":
        game1 = TicTacToe("O")
    else:
        print("You have an invalid option. The system will now shut down!")
        sys.exit()

