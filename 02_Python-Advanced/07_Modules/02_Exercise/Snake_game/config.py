FPS = 10

DISPLAY_SIZE = 800
SCALE = 20
GRIND_SIZE = DISPLAY_SIZE // SCALE

DIRECTIONS = {
              "UP": 0,
              "DOWN": 1,
              "LEFT": 2,
              "RIGHT": 3
              }
       
DIRECTION_TRANSFORM = {  
                    DIRECTIONS['UP']: [0, -1],
                    DIRECTIONS['DOWN']: [0, 1],
                    DIRECTIONS['LEFT']: [-1, 0],
                    DIRECTIONS['RIGHT']: [1, 0]
                    }
