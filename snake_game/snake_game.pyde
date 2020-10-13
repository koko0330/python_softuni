import config
import snake
import food
import score
import os


def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(10)
    
    if os.path.exists(config.HIGHSCORE_FILE_PATH):
        with open(config.HIGHSCORE_FILE_PATH, "r") as file:
            score.highscore = int(file.read())
        
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    score.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
        score.score += 1
        
    if snake.eats_self():
        print("GAME OVER")
        score.set_highscore()
        noLoop()
    

    
def keyPressed():
    if keyCode == UP and config.CURRENT_DIR != "down":
        config.CURRENT_DIR = "up"
        
    elif keyCode == DOWN and config.CURRENT_DIR != "up":
        config.CURRENT_DIR = "down"
        
    elif keyCode == RIGHT and config.CURRENT_DIR != "left":
        config.CURRENT_DIR = "right"
        
    elif keyCode == LEFT and config.CURRENT_DIR != "right":
        config.CURRENT_DIR = "left"
        
