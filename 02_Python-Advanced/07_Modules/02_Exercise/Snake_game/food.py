import config

def get_random_coord():
    return int(random(config.GRIND_SIZE))

food_pos = [
            get_random_coord(), 
            get_random_coord()
            ]

def draw_food():
    fill(0 , 255, 0)
    rect(
         food_pos[0] * config.SCALE,
         food_pos[1] * config.SCALE,
         config.SCALE,
         config.SCALE
         )

def respawn():
    food_pos[0] = get_random_coord()
    food_pos[1] = get_random_coord()
