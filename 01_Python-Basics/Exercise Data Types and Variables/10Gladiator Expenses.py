lost_games = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
prince = 0

for i in range(1, lost_games+1):
    if i % 12 == 0:
        prince += armor
    if i % 6 == 0:
        prince += shield
    if i % 3 == 0:
        prince += sword
    if i % 2 == 0:
        prince += helmet

print(f"Gladiator expenses: {prince:.2f} aureus")




