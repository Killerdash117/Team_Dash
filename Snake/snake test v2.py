import pygame, sys, time, random
from pygame.locals import *

#CHANGABLES
width = 190
height = 110
scale = 5
seg_size = 3
fps = 2

pygame.init()

fpsClock = pygame.time.Clock()

playSurf = pygame.display.set_mode((width * scale, height * scale))
pygame.display.set_caption('i like pizza')

red = pygame.Color(225, 0, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(225, 255, 255)
grey = pygame.Color(150, 150, 150)

snakePos = [5 * scale * seg_size, 5 * scale * seg_size]
snakeSeg = [[5 * scale * seg_size, 5 * scale * seg_size],[4 * scale * seg_size, 5 * scale * seg_size], [3 * scale * seg_size, 5 * scale * seg_size]]
raspPos = [random.randint(1, int(width/seg_size)) * scale * seg_size, random.randint(1, int(height/seg_size)) * scale * seg_size]
raspSpawn = 2
direction = 'right'
changeDir = direction

def gameOver():
    gOFont = pygame.font.Font('freesansbold.ttf', round(3.6 * scale))
    gOSurf = gOFont.render('you are fucking shit my nig', True, grey)
    gORect = gOSurf.get_rect()
    gORect.midtop = (scale * width/2, scale*6)
    playSurf.blit(gOSurf, gORect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDir = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDir = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDir = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDir = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changeDir == 'right' and not direction == 'left':
        direction = changeDir
    if changeDir == 'left' and not direction == 'right':
        direction = changeDir
    if changeDir == 'up' and not direction == 'down':
        direction = changeDir
    if changeDir == 'down' and not direction == 'up':
        direction = changeDir

    if direction == 'right':
        snakePos[0] += scale * seg_size
    if direction == 'left':
        snakePos[0] -= scale * seg_size
    if direction == 'up':
        snakePos[1] -= scale * seg_size
    if direction == 'down':
        snakePos[1] += scale * seg_size

    snakeSeg.insert(0, list(snakePos))

    if snakePos[0] == raspPos[0] and snakePos[1] == raspPos[1]:
        raspSpawn = 0
    else:
        snakeSeg.pop()

    if raspSpawn == 0:
        x = round(random.randrange(1, int(width * (1/seg_size))))
        y = round(random.randrange(1, int(height * (1/seg_size))))
        raspPos = [int(x*scale * seg_size), int(y*scale * seg_size)]
        raspSpawn = 1

    playSurf.fill(black)

    i = 0
    for pos in snakeSeg:
        pygame.draw.rect(playSurf, white, Rect(pos[0], pos[1], scale * seg_size, scale * seg_size))
        if snakePos[0] == pos[0] and snakePos[1] == pos[1] and i != 0:
            gameOver()
        else:
            i += 1
    pygame.draw.rect(playSurf, red, Rect(raspPos[0], raspPos[1], scale * seg_size, scale * seg_size))
    pygame.display.flip()

    if snakePos[0] > (width - 1) * scale or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > (height - 1) * scale or snakePos[1] < 0:
        gameOver()

    fpsClock.tick(fps)

