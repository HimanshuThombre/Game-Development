import pygame
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((900, 700),pygame.RESIZABLE)
isRunning = True

pygame.display.set_caption('Bouncing Ball')
icon = pygame.image.load('BB_ball1.png')
pygame.display.set_icon(icon)

block = pygame.image.load("BB_block.png")
blockX = 300
blockY = 500
changeX = 0

ball = pygame.image.load('BB_ball1.png')
ballX = random.randint(0,10)
ballY = 100
Xchange = 0.4
Ychange = 0.4

score = 0
font = pygame.font.SysFont('calibri',36,bold=True)

def displayScore(score):
    scoreImage = font.render(str(score), True, (255, 255, 255))
    screen.blit(scoreImage, (20, 20))


def game_over():
    gfont = pygame.font.SysFont('calibri',36,bold=True)
    game = gfont.render("Game Over!", True, (255, 255, 255))
    game2 = gfont.render("Your Score : " + str(score), True, (255, 255, 255))
    screen.blit(game, (275, 275))
    screen.blit(game2, (275, 330))


isGameOver = False

background = mixer.music.load("BB_music.mp3")
mixer.music.play(-1)  #play music on repeat.

while (isRunning):
    screen.fill((69, 68, 65))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX -= 1
            if event.key == pygame.K_RIGHT:
                changeX += 1

        if event.type == pygame.KEYUP:
            changeX = 0

    if blockX + changeX >= 665 or blockX + changeX < 0:#check if block is touching the boundaries, if yes then stop.
        changeX = 0
    else:
        blockX += changeX

    #change the position of the ball, everytime the loop executes
    ballX += Xchange
    ballY += Ychange

    if (ballX < 0):      #check if the ball is touching any boundaries except the bottom one.
        Xchange = 1
    elif ballX > 836:  # maximum X value of ball in horizontal direction
        Xchange = -1    #changes the movement of ball in opposite direction
    elif ballY < 0:
        Ychange *= -1  #changes the movement of ball in opposite direction

    if ballY >= 570:  #checks if the ball has misses the block
        isGameOver = True
    elif ballX > (blockX + changeX) and ballX < (blockX + changeX + 354) and ballY >= 555:  # To check if the ball has touched the block
        Ychange += -1
        score += 1
        sound = mixer.Sound('BB_Beep Sound .mp3')
        sound.play()

    displayScore(score)
    if (isGameOver):
        game_over()
        pygame.mixer.music.stop()
    else:
        screen.blit(ball, (ballX, ballY))
        screen.blit(block, (blockX, blockY))

    pygame.display.update()
