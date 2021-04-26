from .board import Board, Grid
from .player import Player

if __name__ == "__main__":
    game_board = Board()

    players = [Player() for _ in range(2)]

    current_turn = 0
    i = 0
    turns = 3

    def to_coord(n: str) -> int:
        return int(n) - 1

    while i < turns:
        print(game_board)
        current_player = players[current_turn]
        print(current_player.number)

        try:
            this_x, this_y = list(map(to_coord, input("Enter grid x, y to place your piece").split(", ")))

            this_grid = Grid(this_x, this_y, current_player)
            if game_board.set_grid(this_grid):
                i += 1
                current_turn = (current_turn + 1) % 2

        except ValueError:
            print("Choose a valid coordinate in the form 'x, y'")

    print(game_board)

