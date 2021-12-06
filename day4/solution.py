import numpy as np

class Board:
    def __init__(self, board_list):
        self.array = np.asarray(board_list)
    
    def lines(self):
        return self.array.tolist() + self.array.T.tolist()

    def bingo(self, drawn_numbers):
        return any(map(drawn_numbers.issuperset, self.lines()))
    
    def sum_of_unmarked(self, drawn_numbers):
        return sum(set(self.array.flat) - drawn_numbers)


class Game:
    def __init__(self, numbers, boards):
        self.remaining_numbers = iter(numbers)
        self.drawn_numbers = set()
        self.boards = set(map(Board, boards))
        
    def draw_one(self):
        new_number = next(self.remaining_numbers)
        self.drawn_numbers.add(new_number)
        return new_number

    def play_one_round(self):
        new_number = self.draw_one()
        winning_boards = {board for board in self.boards
                          if board.bingo(self.drawn_numbers)}
        return new_number, winning_boards
    
    def play(self, stop_on_first_win):
        while True:
            new_number, winning_boards = self.play_one_round()
            self.boards -= winning_boards
            if stop_on_first_win and winning_boards or not self.boards:
                board = winning_boards.pop()
                return new_number * board.sum_of_unmarked(self.drawn_numbers)


def read_input(filename):
    with open(filename) as f:
        bingo_numbers = list(map(int, f.readline().strip().split(',')))
        f.readline()

        boards = []
        current_board = []
        for line in f:
            if nums := list(map(int, line.strip().split())):
                current_board.append(nums)
            else:
                boards.append(current_board)
                current_board = []            

    return bingo_numbers, boards


if __name__ == "__main__":
    numbers, boards = read_input('day4/input.txt')
    print(f'Part A: {Game(numbers, boards).play(stop_on_first_win=True)=}')
    print(f'Part B: {Game(numbers, boards).play(stop_on_first_win=False)=}')