import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('music kit')
label_font = pygame.font.Font('FreeSansBold.ttf', 30)

fps = 60
timer = pygame.time.Clock()

def draw_grid():
    left_box = python.draw.rect(screen, gray, [0,0,200,HEIGHT], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, white]
    hi_hat_text = label_font.render('Hi Hat', True)

run = True 
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get(): #any event taking place
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()


