import pygame
from pygame import mixer
pygame.init()
WIDTH = 1400
HEIGHT = 800
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green=(0,255,0)
gold=(212,175,55)
blue=(0,255,255)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('music kit')
label_font = pygame.font.Font('FreeSansBold.ttf', 30)
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm=240
playing=True
active_length=0
active_beat=1
beat_changed=True

#load in sounds
hi_hat=mixer.Sound('sounds\hi hat.WAV')
snare=mixer.Sound('sounds\snare.WAV')
kick=mixer.Sound('sounds\kick.WAV')
crash=mixer.Sound('sounds\crash.WAV')
clap=mixer.Sound('sounds\clap.WAV')
tom=mixer.Sound('sounds\\tom.WAV')

def draw_grid(clicks,beat):
    left_box = pygame.draw.rect(screen, gray, [0,0, 200,HEIGHT - 195], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, white]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (50, 30))
    Snare_text = label_font.render('Snare', True, white)
    screen.blit(Snare_text, (50, 130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (24, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (53, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (65, 430))
    floor_tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_tom_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)
# for i in range(beats):
#     for j in range(instruments):
#         rect = pygame.draw.rect(screen, gray, [i * ((WIDTH - 200) // beats) + 205, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200)//instruments)], 5, 5)
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i]==-1:
                color=gray
            else:
                color=green
            rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 200) // beats) + 211, (j * 100)+3, ((WIDTH - 200) // beats)-10, ((HEIGHT - 200)//instruments)-10], 0 ,3 )
            rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 200) // beats) + 205, (j * 100)+3, ((WIDTH - 200) // beats)-5, ((HEIGHT - 200)//instruments)-5], 0 , 3)
            pygame.draw.rect(screen, gold, [i * ((WIDTH - 200) // beats) + 205, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200)//instruments)], 5, 5)
            pygame.draw.rect(screen, black, [i * ((WIDTH - 200) // beats) + 205, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200)//instruments)], 2, 5)
            boxes.append((rect, (i, j)))
        
        active=pygame.draw.rect(screen,blue,[beat*((WIDTH-197)//beats)+205,0,((WIDTH-200)//beats),instruments*100],5,3)
    return boxes
run = True 
while run:
    timer.tick(fps)
    screen.fill(black)
    #draw_grid()
    boxes = draw_grid(clicked,active_beat)
    for event in pygame.event.get(): #any event taking place
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos): #position at which mouse down occur
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
    beat_length=3600//bpm

    if playing:
        if active_length < beat_length:
            active_length+=1
        else:
            active_length=0
            if active_beat<beats-1:
                active_beat+=1
                beat_changed=True
            else:
                active_beat=0
                beat_changed=True


            
    pygame.display.flip()
pygame.quit()
