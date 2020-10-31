import config 

current_direction = config.DIRECTIONS["RIGHT"]
snake_pos = [
             [0, 0],
             [1, 0],
             [2, 0]
             ]

def draw_snake():
    fill(255)
    
    for x, y in snake_pos:
        rect(x * config.SCALE , 
             y * config.SCALE , 
             config.SCALE , 
             config.SCALE)
        

def move():
    head = snake_pos[-1]
    body = snake_pos[:-1]
    
    
    for i in range(len(body)):
        snake_pos[i][0] = snake_pos[i+1][0]
        snake_pos[i][1] = snake_pos[i+1][1]
    
    inc_x, inc_y = config.DIRECTION_TRANSFORM[current_direction]
    head[0] += inc_x
    head[1] += inc_y
    
    if head[0] < 0: 
        head[0] = config.GRIND_SIZE
    if head[0] > config.GRIND_SIZE: 
        head[0] = 0    
    if head[1] < 0: 
        head[1] = config.GRIND_SIZE
    if head[1] > config.GRIND_SIZE: 
        head[1] = 0
         
    
def change_direction(direction):
    global current_direction
    current_direction = direction
    
def can_eat_food(food_pos):
    head = snake_pos[-1]
    return head == food_pos
    
def grow():
    global snake_pos    
    snake_pos = [[snake_pos[0][0],snake_pos[0][1]]] + snake_pos

def is_dead():
    head = snake_pos[-1]
    body = snake_pos[:-1]
    
    for body_part in body:
        if haed == body_part
            return True 
    
    return False
