import math
year = str(input())
holidays = int(input())
trips = int(input())

weeks_in_sofia = (48-trips)*3/4
holidays = holidays * 2/3
games = trips + weeks_in_sofia + holidays

if year == "leap":
    games *= 1.15

games=math.floor(games)

print(games)

