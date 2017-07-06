import pygame, sys, time, random
from pygame.locals import *

width = 33
height = 25
scale = 29

pygame.init()

fpsClock = pygame.time.Clock()

playSurf = pygame.display.set_mode((width * scale, height * scale))
pygame.display.set_caption('SNAAAAAAAKKKE!')

red = pygame.Color(225, 0, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(225, 255, 255)
grey = pygame.Color(150, 150, 150)
blue = pygame.Color(100, 100, 255)

snakePos1 = [25 * scale, 5 * scale]
snakeSeg1 = [[25 * scale, 5 * scale],[24 * scale, 5 * scale], [23 * scale, 5 * scale]]
raspPos = [15 * scale, 15 * scale]
raspSpawn = 1
direction1 = 'down'
changeDir1 = direction1

snakePos2 = [5 * scale, 5 * scale]
snakeSeg2 = [[5 * scale, 5 * scale],[4 * scale, 5 * scale], [3 * scale, 5 * scale]]
direction2 = 'down'
changeDir2 = direction2

def gameOver1():
    gOFont = pygame.font.Font('freesansbold.ttf', round(3.6 * scale))
    gOSurf = gOFont.render('Player 1 Wins', True, grey)
    gORect = gOSurf.get_rect()
    gORect.midtop = (scale * 16, scale/2)
    playSurf.blit(gOSurf, gORect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def gameOver2():
    gOFont = pygame.font.Font('freesansbold.ttf', round(3.6 * scale))
    gOSurf = gOFont.render('Player 2 Wins', True, grey)
    gORect = gOSurf.get_rect()
    gORect.midtop = (scale * 16, scale/2)
    playSurf.blit(gOSurf, gORect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
#snake 1    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                changeDir1 = 'right'
            if event.key == K_LEFT:
                changeDir1 = 'left'
            if event.key == K_UP:
                changeDir1 = 'up'
            if event.key == K_DOWN:
                changeDir1 = 'down'
            if event.key == ord('d'):
                changeDir2 = 'right'
            if event.key == ord('a'):
                changeDir2 = 'left'
            if event.key == ord('w'):
                changeDir2 = 'up'
            if event.key == ord('s'):
                changeDir2 = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changeDir1 == 'right' and not direction1 == 'left':
        direction1 = changeDir1
    if changeDir1 == 'left' and not direction1 == 'right':
        direction1 = changeDir1
    if changeDir1 == 'up' and not direction1 == 'down':
        direction1 = changeDir1
    if changeDir1 == 'down' and not direction1 == 'up':
        direction1 = changeDir1

    if direction1 == 'right':
        snakePos1[0] += scale
    if direction1 == 'left':
        snakePos1[0] -= scale
    if direction1 == 'up':
        snakePos1[1] -= scale
    if direction1 == 'down':
        snakePos1[1] += scale

    snakeSeg1.insert(0, list(snakePos1))

    if snakePos1[0] == raspPos[0] and snakePos1[1] == raspPos[1]:
        raspSpawn = 0
    else:
        snakeSeg1.pop()
#snake 2
    if changeDir2 == 'right' and not direction2 == 'left':
        direction2 = changeDir2
    if changeDir2 == 'left' and not direction2 == 'right':
        direction2 = changeDir2
    if changeDir2 == 'up' and not direction2 == 'down':
        direction2 = changeDir2
    if changeDir2 == 'down' and not direction2 == 'up':
        direction2 = changeDir2

    if direction2 == 'right':
        snakePos2[0] += scale
    if direction2 == 'left':
        snakePos2[0] -= scale
    if direction2 == 'up':
        snakePos2[1] -= scale
    if direction2 == 'down':
        snakePos2[1] += scale
    

    snakeSeg2.insert(0, list(snakePos2))

    if snakePos2[0] == raspPos[0] and snakePos2[1] == raspPos[1]:
        raspSpawn = 0
    else:
        snakeSeg2.pop()

    if raspSpawn == 0:
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        raspPos = [int(x*scale), int(y*scale)]
        raspSpawn = 1

    playSurf.fill(black)
    i = 0
    for pos in snakeSeg2:
        pygame.draw.rect(playSurf, white, Rect(pos[0], pos[1], scale, scale))
        if snakePos1[0] == pos[0] and snakePos1[1] == pos[1] and i != 0:
            gameOver1()
        else:
            i += 1

    i = 0
    for pos in snakeSeg1:
        pygame.draw.rect(playSurf, blue, Rect(pos[0], pos[1], scale, scale))
        if snakePos2[0] == pos[0] and snakePos2[1] == pos[1] and i != 0:
            gameOver2()
        else:
            i += 1
            
    pygame.draw.rect(playSurf, red, Rect(raspPos[0], raspPos[1], scale, scale))
    pygame.display.flip()

    if snakePos1[0] > 31 * scale or snakePos1[0] < 0:
        gameOver1()
    if snakePos1[1] > 23 * scale or snakePos1[1] < 0:
        gameOver1()
    
    if snakePos2[0] > 31 * scale or snakePos2[0] < 0:
        gameOver2()
    if snakePos2[1] > 23 * scale or snakePos2[1] < 0:
        gameOver2()

    fpsClock.tick(11)
