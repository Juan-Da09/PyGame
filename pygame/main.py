WIDTH = 800
HEIGHT = 600

player = Actor("player",(400, 500))
coin = Actor("coin")
impostor = Actor("impostor")

score = 0
game_over = False

def draw():
    screen.clear()
    screen.fill((30,30,40))

    player.draw()
    coin.draw()
    impostor.draw()

    screen.draw.text(f"Puntos: {score}", (10, 10), fontsize=40, color="white")

    if game_over:
        screen.draw.text("GAME OVER", (WIDTH/2, HEIGHT/2), fontaize=80, color="red")


import random

def move_coin():
    coin.y += 4
    if coin.y > HEIGHT:
        reset_coin()
           
def reset_coin():
    coin.pos = (random.randint(50, WIDTH-50),0)

def move_impostor():
    impostor.y += 6
    if impostor.y > HEIGHT:
        reset_impostor()

def reset_impostor():
    impostor.pos = (random.randint(50, WIDTH-50),0)
    
def check_collision():
        global score, game_over
        
    if player.colliderect(coin):
        score += 1
        reset_coin()
        
    if player.colliderect(impostor):
        game_over = True
        
        


def update():
    if game_over:
        return

    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5
        
    if player.x < 40:
        player.x = 40
        
    if player.x > WIDTH - 40:
        player.x = WIDTH - 40
        
    move_coin
    move_impostor
    check_collision                                                                               
