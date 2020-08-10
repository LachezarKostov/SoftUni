walk_time = int(input())
num_of_walks = int(input())
calories = int(input())

colories_par_day = walk_time*num_of_walks*5
if colories_par_day >= (calories/2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {colories_par_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {colories_par_day}.")