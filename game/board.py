import blessed
from typing import Optional

from .player import Player

TERM = blessed.Terminal()


class Grid:
    def __init__(self, x_pos: int, y_pos: int, player: Optional[Player] = None):
        self.x = x_pos
        self.y = y_pos
        self.player = player

    def __str__(self):
        return self.create_grid()

    def create_grid(self) -> str:
        return str(self.player) if self.player else "."

    def __repr__(self):
        return self.create_grid()


class Board:
    def __init__(self, size: int = 19):
        self.size = size
        self._board = []

    def __str__(self):
        return self.create_board()

    def create_board(self) -> blessed.Terminal:
        total_characters = self.size * 3
        refresh_board = ""
        horizontal_edge = f" {'=' * total_characters} \n"
        refresh_board += horizontal_edge
        for y_position in range(self.size):
            this_row = "|"
            grid_char_pos = 0
            for x_position in range(total_characters):
                if grid_char_pos == 1:
                    this_row += str(self.board[y_position][x_position // 3])
                else:
                    this_row += "-"
                grid_char_pos = (grid_char_pos + 1) % 3
            this_row += "|\n"
            refresh_board += this_row
        refresh_board += horizontal_edge

        return TERM.home + TERM.clear + refresh_board

    @property
    def board(self):
        if self._board == []:
            board_dimensions = range(self.size + 1)
            for y in board_dimensions:
                this_row = []
                for x in board_dimensions:
                    this_row.append(Grid(x, y))
                self._board.append(this_row)

        return self._board

    def set_grid(self, grid: Grid) -> bool:
        try:
            if self.board[grid.y][grid.x].player is None:
                self.board[grid.y][grid.x] = grid
                return True
            print("Space is occupied")
            return False
        except KeyError:
            print("Invalid grid position")
            return False
