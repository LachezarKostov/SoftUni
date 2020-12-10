from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f"Player {player.username} already exists!")
        else:
            self.players.append(player)
            self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        list_of_players_names = [p.username for p in self.players]
        index = list_of_players_names.index(player)
        self.players.pop(index)
        self.count -= 1

    def find(self, name: str):
        list_of_players_names = [p.username for p in self.players]
        index = list_of_players_names.index(name)
        return self.players[index]

