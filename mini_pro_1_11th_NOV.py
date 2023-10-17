#   Project : Game Development using Python (PyGame)
#   Author  : Abhishek Jadhao

import random
import time

import pygame
from pygame import mixer

pygame.init()  # Game Initialised

winHeight = 450
winWidth = 450

#   colors :
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
fps = 500

font = pygame.font.SysFont('calibri', 40, bold=True)


def screenScore(text, color, x, y):
    textScore = font.render(text, True, color)
    win.blit(textScore, [x, y])


def plotSnake(win, color, snakeList, snakeSize):
    for x, y in snakeList:
        snake = pygame.draw.rect(win, color, [x, y, snakeSize, snakeSize])


#   Game Display
win = pygame.display.set_mode((winHeight, winWidth), pygame.RESIZABLE)

pygame.display.set_caption("SNake Game")
pygame.display.update()


def gameLoop():
    # Background Sounds
    mixer.music.load('snkbgmsic.mp3')
    mixer.music.play(-1)

    #   About Snake
    exitGame = False
    gameOver = False
    snakeX = 60
    snakeY = 60
    velocityX = 0
    velocityY = 0
    initVel = 0.5
    snakeSize = 20
    foodX = random.randrange(20, 400, 20)
    foodY = random.randrange(20, 400, 20)
    clock = pygame.time.Clock()
    snakeList = []
    snakeLength = 1

    score = 0

    while not exitGame:

        if gameOver:
            pygame.mixer.music.stop()
            win.fill((0, 0, 255))
            screenScore('Game Over !', red, 120, 100)
            screenScore('Press Enter', red, 120, 160)
            screenScore('To', red, 210, 200)
            screenScore(' Continue', red, 120, 240)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityX = velocityX + initVel
                        velocityY = 0
                    if event.key == pygame.K_LEFT:
                        velocityX = velocityX - initVel
                        velocityY = 0
                    if event.key == pygame.K_UP:
                        velocityY = velocityY - initVel
                        velocityX = 0
                    if event.key == pygame.K_DOWN:
                        velocityY = velocityY + initVel
                        velocityX = 0
                    if event.key == pygame.K_q:
                        score += 50

                if event.type == pygame.KEYUP:
                    velocityX = 0
                    velocityY = 0

            snakeX += velocityX
            snakeY += velocityY

            if abs(snakeX - foodX) < 20 and abs(snakeY - foodY) < 20:
                score += 10
                foodX = random.randrange(20, winWidth, 20)
                foodY = random.randrange(20, winHeight, 20)
                snakeLength += 40

            win.fill((0, 255, 0))
            screenScore(" Score : " + str(score), blue, 5, 5)
            food = pygame.draw.rect(win, red, [foodX, foodY, snakeSize, snakeSize])

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)

            if len(snakeList) > snakeLength:
                del snakeList[0]

            #for segment in snakeList:
             #   if segment.__len__(head) < 20:
              #      time.sleep(1)
               #     head.goto(0, 0)

            if snakeX < 0 or snakeX > winWidth - 20 or snakeY < 0 or snakeY > winHeight - 20:
                gameOver = True
                print('Game Over')

            # snake = pygame.draw.rect(win, black, [snakeX, snakeY, snakeSize, snakeSize])
            plotSnake(win, black, snakeList, snakeSize)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()



gameLoop()

