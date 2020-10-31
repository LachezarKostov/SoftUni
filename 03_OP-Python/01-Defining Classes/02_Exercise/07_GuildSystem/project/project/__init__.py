from project.player import Player
from project.guild import Guild

player_1 = Player("P1", 100, 100)
player_2 = Player("P2", 100, 100)
player_3 = Player("P2", 100, 100)
print(player_1.add_skill("S1", 50))
print(player_1.add_skill("S1", 50))
print(player_1.add_skill("S1", 60))
print(player_1.add_skill("S2", 60))
print(player_1.player_info())

guild1 = Guild("G1")
guild2 = Guild("G2")

print(guild1.assign_player(player_1))
print(guild1.assign_player(player_1))
print(guild1.assign_player(player_2))
print(guild2.assign_player(player_1))
print(guild1.assign_player(player_3))

print(guild1.kick_player("P1"))
print(guild1.kick_player("P1"))

print(guild1.guild_info())

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())



