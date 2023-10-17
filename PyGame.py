import pygame
import sys, os, time


# import mini_pro_2_11th_NOV


pygame.init()
pygame.get_init()

clk = pygame.time.Clock()
fps = 100


# Font


def showText(text, color, x, y, size):
    font = pygame.font.SysFont('calibri', size, bold=True)
    buttonText = font.render(text, True, color)
    screen.blit(buttonText, [x, y])


def showDevelopers(text, color, x, y, size):
    font2 = pygame.font.SysFont('calibri', size, bold=True)
    buttonText2 = font2.render(text, True, color)
    screen.blit(buttonText2, [x, y])


# Display
screenHeight = 415
screenWidth = 860
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Games")
icon = pygame.image.load("developer-api-coding-screen-512.png")
pygame.display.set_icon(icon)
screen.fill((0, 255, 0))

# gameWindow
gameWindowColor = (255, 255, 255)
gameWindowHeight = 355
gameWindowWidth = 500
gagameWindow = pygame.draw.rect(screen, gameWindowColor, [30, 30, gameWindowWidth, gameWindowHeight], border_radius=5)

# LoginEindow
loginWindowColor = (255, 255, 255)
loginWindowHeight = 355
loginWindowWidth = 270
loginWindow = pygame.draw.rect(screen, loginWindowColor, [560, 30, loginWindowWidth, loginWindowHeight],
                               border_radius=5)
showDevelopers('Developers', (0, 0, 0), 580, 50, 48)
pygame.draw.line(screen, (0, 0, 0), (575, 90), (810, 90))
showText('Er. Abhishek Jadhao', (0, 0, 0), 580, 120, 24)
showText('Er. Himanshu Thombre', (0, 0, 0), 580, 148, 24)
showText('Er. Kunal Kolse', (0, 0, 0), 580, 176, 24)
showDevelopers('Guided by: ', (0, 0, 0), 580, 230, 32)
pygame.draw.line(screen, (0, 0, 0), (575, 260), (730, 260))
showText('Prof. S. A. Bachwani', (0, 0, 0), 580, 280, 24)

# game Icons
gIconColor = (255, 255, 0)
iconHeight = 120
iconWidth = 120

gOne = pygame.draw.rect(screen, gIconColor, [65, 65, iconWidth, iconHeight])
imgOne = pygame.image.load('snake.png')
showText('Snake Game', (0, 0, 255), 90, 172, 12)
screen.blit(imgOne, (75, 70))

gTwo = pygame.draw.rect(screen, gIconColor, [65, 220, iconWidth, iconHeight])
imgTwo = pygame.image.load('extraterrestrial.png')
showText('Ghost Riders', (0, 0, 255), 90, 330, 12)
screen.blit(imgTwo, (75, 225))

gThree = pygame.draw.rect(screen, gIconColor, [220, 65, iconWidth, iconHeight])
imgThree = pygame.image.load('ballIcon.png')
showText('Bouncing Ball', (0, 0, 255), 250, 172, 12)
screen.blit(imgThree, (230, 70))

gFour = pygame.draw.rect(screen, gIconColor, [220, 220, iconWidth, iconHeight])
imgFour = pygame.image.load('birdIcon.png')
showText('Flappy Bird', (0, 0, 255), 250, 325, 12)
screen.blit(imgFour, (230, 220))

gFive = pygame.draw.rect(screen, gIconColor, [375, 65, iconWidth, iconHeight])
imgFive = pygame.image.load('egg_catcher.png')
showText('Egg Catcher', (0, 0, 255), 405, 172, 12)
screen.blit(imgFive, (385, 70))

gSix = pygame.draw.rect(screen, gIconColor, [375, 220, iconWidth, iconHeight])
imgSix = pygame.image.load('tic_tac.png')
showText('Tic Tac Toe', (0, 0, 255), 405, 325, 12)
screen.blit(imgSix, (385, 220))

# Mouse Event

clk.tick(fps)
pygame.display.update()
On = True
while On:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            On = False
            # exit()

    pos = pygame.mouse.get_pos()

    if gOne.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            import mini_pro_1_11th_NOV

            break

    if gTwo.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            import mini_pro_2_11th_NOV

            break

    if gThree.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            import main

            break

    #if gFour.collidepoint(pos):
     #   if pygame.mouse.get_pressed()[0] == 1:
      #      import mini_pro_1_11th_NOV

       #     break

    if gFive.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            import egg_catcher

            break

    if gSix.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            import tic_t

            break
