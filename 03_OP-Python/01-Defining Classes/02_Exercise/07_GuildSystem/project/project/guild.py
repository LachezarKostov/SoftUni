from typing import List
from project.player import Player


class Guild:
    name: str
    list_of_players = List[Player]

    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):

        if player.name in [p.name for p in self.list_of_players]:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.list_of_players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        players_by_name = [p.name for p in self.list_of_players]

        if player_name not in players_by_name:
            return f"Player {player_name} is not in the guild."

        del self.list_of_players[players_by_name.index(player_name)]
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + \
               "".join([p.player_info() for p in self.list_of_players])
