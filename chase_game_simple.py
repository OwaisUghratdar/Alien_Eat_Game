import random

WIDTH = 600
HEIGHT = 600

player = Actor("alien")
player.x = 200
player.y = 200

enemy = Actor("monster")
coin = Actor("coin", pos=(300,300))
score = 0
time = 20


def draw():
    screen.clear()
    player.draw()
    enemy.draw()
    coin.draw()
    screen.draw.text("Alien Game", (250,10), color='orange')
    screen.draw.text("Collect coins, don't let the monster get you", (140,30), color='yellow')
    screen.draw.text("Score:", (30,550), color='green')
    score_string = str(score)
    screen.draw.text(score_string, (100,550), color='green')
    time_string = str(round(time))
    screen.draw.text(time_string, (0,0), color='pink')

def update(delta):
    global score, time
    time = time - delta
    if time <= 0:
        exit()
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

    if enemy.x < player.x:
        enemy.x = enemy.x + 0.1
    if enemy.x > player.x:
        enemy.x = enemy.x - 0.1
    if enemy.y < player.y:
        enemy.y = enemy.y + 0.1
    if enemy.y > player.y:
        enemy.y = enemy.y - 0.1
    if player.colliderect(enemy):
        exit()

    if coin.colliderect(player):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)