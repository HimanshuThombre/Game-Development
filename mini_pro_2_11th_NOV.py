import math
import pygame
import random
from pygame import mixer




# Initialize the pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Background Sounds
mixer.music.load('background.wav')
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Players
playerImg = pygame.image.load('playerImg.png')
playerX = 370  # random.randrange(0, 700, 10)
playerY = 480  # random.randrange(500, 550, 10)
changX = 0
changeY = 0

# Enemy
playerEnemy = []
playerEnemyX = []
playerEnemyY = []
enemychangeX = []
enemychangeY = []
numOfEnemy = 7

for i in range(numOfEnemy):
    playerEnemy.append(pygame.image.load('enemy.png'))
    playerEnemyX.append(random.randint(0, 735))
    playerEnemyY.append(random.randint(50, 150))
    enemychangeX.append(3)
    enemychangeY.append(20)

# Bullets
bulletImg = pygame.image.load('bull_prev_ui.png')
bulletX = 0
bulletY = 480
bulletChangeX = 0
bulletChangeY = 20
bulletState = 'ready'  # Ready- you can't see bullet on the screen

# score
scoreValue = 0
font = pygame.font.SysFont('calibri', 40, bold=True)
textX = 10
textY = 10

# gameOver Text
overfont = pygame.font.SysFont('calibri', 40, bold=True)

def showScore(x, y):
    score = font.render("Score : " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))

def gameOverText():
    gOverText = overfont.render("Game Over", True, (255, 0, 0))
    screen.blit(gOverText, (250, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))

def gameWin():
    screen.fill((255, 0, 0))
    gameWin = overfont.render("You Won !", True, (255, 255, 255))
    screen.blit(gameWin, (250, 250))


def enemy(x, y, i):
    screen.blit(playerEnemy[i], (x, y))


def fireBullets(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(playerEnemyX, playerEnemyY, bulletX, bulletY):
    dist = math.sqrt(math.pow((playerEnemyX - bulletX), 2) + math.pow((playerEnemyY - bulletY), 2))
    if dist < 27:
        return True
    else:
        return False


running = True

while running:

    # RGB = Red Green Blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    #if scoreValue
    if scoreValue >= 1000:
        gameWin()


    pos = pygame.mouse.get_pos()
    #print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changX = -2
                changeY = 0
            if event.key == pygame.K_RIGHT:
                changX = 2
                changeY = 0
            if event.key == pygame.K_UP:
                changeY = -2
                changX = 0
            if event.key == pygame.K_DOWN:
                changeY = 2
                changX = 0

            #if event.key == pygame.K_q:
             #   scoreValue += 50

            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fireBullets(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            changX = 0
            changeY = 0

    playerX += changX
    playerY += changeY

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Enemy Movements
    for i in range(numOfEnemy):
        # Game Over
        if playerEnemyY[i] > 440 or (abs(playerX - playerEnemyX[i]) < 32 and abs(playerY - playerEnemyY[i]) < 32):
            screen.fill((0, 255, 0))
            for j in range(numOfEnemy):
                playerEnemyY[j] = 2000

            gameOverText()
            break

        playerEnemyX[i] += enemychangeX[i]
        if playerEnemyX[i] <= 0:
            enemychangeX[i] = 3
            playerEnemyY[i] += enemychangeY[i]
        elif playerEnemyX[i] >= 736:
            enemychangeX[i] = -3
            playerEnemyY[i] += enemychangeY[i]

        # Collision
        collision = isCollision(playerEnemyX[i], playerEnemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound('explosion.wav')
            explosionSound.play()
            bulletY = 480
            bulletState = "ready"
            scoreValue += 10
            #print(scoreValue)
            playerEnemyX[i] = random.randint(0, 735)
            playerEnemyY[i] = random.randint(50, 150)
        enemy(playerEnemyX[i], playerEnemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState == "fire":
        fireBullets(bulletX, bulletY)
        bulletY -= bulletChangeY

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
