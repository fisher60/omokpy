class Player:
    player_nums = 0

    def __init__(self):
        self.number = self.add_player()

    @staticmethod
    def add_player() -> int:
        Player.player_nums += 1
        return Player.player_nums

    def __str__(self):
        return "X" if self.number == 1 else "O"

    def __repr__(self):
        return f"Player {self.number}"
