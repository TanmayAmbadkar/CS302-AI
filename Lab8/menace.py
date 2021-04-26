import random
from random import choice
from collections import Counter
import json


class Menace:

    def __init__(self):
        self.board = [" "]*9
        self.beads = [10]*9
        # self.matchboxes = {}
        self.movesplayed = []
        try:
            a_file = open("data.json", "r")
            # output = a_file.read()
            self.matchboxes = json.loads(a_file.read())
        except:
            self.matchboxes = {}
            # print("No Pre Game exist")

    def printBoard(self):
        print("\nPositions:")
        print("0 | 1 | 2   ", self.board[0],
              "|", self.board[1], "|", self.board[2])
        print("--+---+--    --+---+--")
        print("3 | 4 | 5   ", self.board[3],
              "|", self.board[4], "|", self.board[5])
        print("--+---+--    --+---+--")
        print("6 | 7 | 8   ", self.board[6],
              "|", self.board[7], "|", self.board[8])
        print("\n")

    def userChance(self):
        pos = int(input("Enter position: "))
        if self.board[pos] != " ":
            print("Wrong input enter again")
            self.userChance()
        else:
            self.board[pos] = "X"

    def compChance(self):
        current_board = self.board_string()
        # print("board", movesplayed)
        if current_board not in self.matchboxes:
            new_beads = [pos for pos, mark in enumerate(
                current_board) if mark == ' ']
            # Early boards start with more beads
            self.matchboxes[current_board] = new_beads * \
                ((len(new_beads) + 2) // 2)

        current_beads = self.matchboxes[current_board]
        if len(current_beads):
            bead = random.choice(current_beads)
            self.movesplayed.append((current_board, bead))
        else:
            bead = -1
        # print(board[bead])
        return bead
        # while (True):
        #     if board[pos] != " ":
        #         used.append(pos)
        #         pos = random.choices(range(0, 9), weights=beads, k=1)[0]
        #     else:
        #         board[pos] = "O"
        #         break

    def winning(self):
        if (self.board[0] != ' ' and
            ((self.board[0] == self.board[1] == self.board[2]) or
             (self.board[0] == self.board[3] == self.board[6]) or
             (self.board[0] == self.board[4] == self.board[8]))) or (self.board[4] != ' ' and
                                                                     ((self.board[1] == self.board[4] == self.board[7]) or
                                                                      (self.board[3] == self.board[4] == self.board[5]) or
                                                                      (self.board[2] == self.board[4] == self.board[6]))) or (self.board[8] != ' ' and
                                                                                                                              ((self.board[2] == self.board[5] == self.board[8]) or
                                                                                                                               (self.board[6] == self.board[7] == self.board[8]))):
            return True
        else:
            return False

    def Tie(self):
        c = Counter(self.board)
        for i in c:
            if (i == " "):
                return False
        return True

    def beadChange(self, n):
        if n == 3:
            for (board, bead) in self.movesplayed:
                self.matchboxes[board].extend([bead, bead, bead])
            # self.num_win += 1
        if n == 2:
            for (board, bead) in self.movesplayed:
                self.matchboxes[board].append(bead)
        if n == 1:
            # Lose, remove a bead
            for (board, bead) in self.movesplayed:
                matchbox = self.matchboxes[board]
                del matchbox[matchbox.index(bead)]

    def resetGame(self):
        self.board = [" "]*9
        self.movesplayed = []

    def board_string(self):
        return ''.join(self.board)

    def playGame(self):
        chance = 0
        while (True):
            chance += 1
            move = self.compChance()
            self.board[move] = "O"
            # if chance>=2:
            if self.winning():
                self.printBoard()
                self.beadChange(3)
                print("Computer Won")
                break
            if self.Tie():
                self.printBoard()
                self.beadChange(2)
                print("Game Tie")
                break
            self.printBoard()
            self.userChance()
            # if chance>=2:
            if self.winning():
                self.printBoard()
                self.beadChange(1)
                print("You Won")
                break

    def instructions(self):
        print("\n")
        print("###########################################################")
        print("Welcome to MENACE Tic Tac Toe")
        print("The computer will gradually learn from the matches")
        print("The difficulty will increase with more number of matches")
        print("You are X and the Computer is O")
        print("Start Playing!")
        print("###########################################################")
        print("\n")

    def exit(self):
        ans = input("\nDo you want to continue? Yes or No \n")
        if ans.lower() == "no":
            print("Thank you for playing!! \n")
            a_file = open("data.json", "w")
            json.dump(self.matchboxes, a_file)
            a_file.close()
            return True
        else:
            a_file = open("data.json", "w")
            json.dump(self.matchboxes, a_file)
            a_file.close()
            return False

    # def Play(self):


if __name__ == '__main__':
    stop = False
    M = Menace()
    while(not stop):
        M.instructions()
        # print("Current beads are: ", Menace.__init__.beads)
        M.playGame()
        # print("Current beads are: ", Menace.beads)
        stop = M.exit()
        M.resetGame()
