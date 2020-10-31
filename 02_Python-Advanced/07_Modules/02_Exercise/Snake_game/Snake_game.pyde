import snake
import config 
import food
import score

def setup():
    frameRate(config.FPS)
    size(config.DISPLAY_SIZE, config.DISPLAY_SIZE)
    
    
def draw():
    background (0)    
    snake.draw_snake()
    snake.move()
    food.draw_food()
    score.draw_score()
    
    if snake.can_eat_food(food.food_pos):
        snake.grow()
        food.respawn()
        score.increase()
        
    
    
    if snake.is_dead():
        print("Game over!")
        noLoop()
    
    
def keyPressed():
    if keyCode == UP:
        snake.change_direction(config.DIRECTIONS["UP"])
    elif keyCode == DOWN:
        snake.change_direction(config.DIRECTIONS["DOWN"])
    elif keyCode == LEFT:
        snake.change_direction(config.DIRECTIONS["LEFT"])
    elif keyCode == RIGHT:
        snake.change_direction(config.DIRECTIONS["RIGHT"])
