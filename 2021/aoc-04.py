__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "05.12.2021"
__email__ = "m@hler.eu"


class Board:
    def __init__(self, board):
        self.board = board
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.matches = [[False] * self.width for nul in range(self.height)]
        self.won = False

    def check_draw(self, draw):
        for row in range(self.width):
            for column in range(self.height):
                if self.board[row][column] == draw:
                    # print(f"Found a match [{self.board[row][column]}] in row [{row+1}] in column [{column+1}]")
                    self.matches[row][column] = True

    def check_winning(self):

        # Check rows for winning
        for row in range(self.width):
            if all([match for match in self.matches[row]]):
                self.won = True
                return True

        # Check columns for winning
        for column in range(self.height):
            col = []
            for row in range(self.width):
                col.append(self.matches[row][column])
            if all([match for match in col]):
                self.won = True
                return True

        return False

    def get_score(self, draw):
        board_sum = 0
        for i in range(self.width):
            for j in range(self.height):
                if not self.matches[i][j]:
                    board_sum += self.board[i][j]

        return board_sum * draw


def get_clean_input():

    with open("inputs/04.txt", "r") as infile:
        all_lines = [line.rstrip() for line in infile.readlines()]
        draws = [int(draw) for draw in all_lines[0].split(",")]

        board = []
        boards = []
        for line in all_lines[2:]:
            if line == "":
                boards.append(board)
                board = []
                continue
            board_line = line.split(" ")
            board_line = [int(num) for num in board_line if num]
            board.append(board_line)
        boards.append(board)

    # [print(board) for board in boards]
    # boards = [Board(board) for board in boards]

    return draws, boards


def first_challenge(draws, boards):
    # First board to win
    for draw in draws:
        for board in boards:
            board.check_draw(draw)
            if board.check_winning():
                return board.get_score(draw)


def second_challenge(draws, boards):
    # Last board to win

    winning_boards = []
    for draw in draws:
        # print(f"\nDraw is [{draw}] | Number of boards is [{len(boards)}]")
        for board in boards:
            board.check_draw(draw)
            old_state = board.won
            if board.check_winning():
                if old_state != board.won:
                    winning_boards.append(board)

                if len(winning_boards) == len(boards):
                    return winning_boards[-1].get_score(draw)


def main():

        draws, boards = get_clean_input()
        print(f"First challenge answer: {first_challenge(draws, [Board(board) for board in boards])}")
        print(f"Second challenge answer: {second_challenge(draws, [Board(board) for board in boards])}")


if __name__ == '__main__':
    main()
