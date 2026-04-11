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


def update():
    if game_over:
        return

    if keyboard.left:
        player.x -= 5

    if keyboard.right:
        player.x += 5                                                                               