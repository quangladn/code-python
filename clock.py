from typing import Text
import pygame, sys, time, math

from pygame import mouse

pygame.init()

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("dong ho dem nguoc")

bg = (155,155,155)
button = (207,207,207)
black = (0,0,0)
font_color = (43,43,43)
red = (255,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()
font = pygame.font.SysFont('sans',50)
font1 = pygame.font.SysFont('sans',90)

mins = 0
secs = 0
total_secs = 0
total = 0
start = False

text_cong = font.render('+',True,black)
text_tru = font.render('-',True,black)
text_min = font.render('min',True,black)
text_sec = font.render('Sec',True,black)
text_reset = font.render('Reset',True,black)
text_start = font.render('Start',True,black)

sound1 = pygame.mixer.Sound('tick.wav')
sound2 = pygame.mixer.Sound('timeout.wav')


while True:
    screen.fill(bg)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (100 < mouse_x < 150) and (50 < mouse_y < 100):
                    total_secs += 60
                    total = total_secs
                if (100 < mouse_x < 150) and (130 < mouse_y < 180):
                    total_secs += 1
                    total = total_secs
                if (350 < mouse_x < 400) and (50 < mouse_y < 100):
                    total_secs -= 60
                    total = total_secs
                if (350 < mouse_x < 400) and (130 < mouse_y < 180):
                    total_secs -= 1
                    total = total_secs
                if (50 < mouse_x < 220) and (200 < mouse_y < 250):
                    start = True
                    total = total_secs
                if (280 < mouse_x < 450) and (200 < mouse_y < 250):
                    total_secs = 0
                    
    
    mins = total_secs//60
    secs = total_secs-(mins*60)

    if start:
        if total_secs > 0:
            pygame.mixer.Sound.play(sound1)
            total_secs -= 1
            time.sleep(1)
        else:
            start = False
            pygame.mixer.Sound.play(sound2)

    pygame.draw.rect(screen,button, (100,50,50,50))
    pygame.draw.rect(screen,button, (100,130,50,50))
    pygame.draw.rect(screen,button, (350,50,50,50))
    pygame.draw.rect(screen,button, (350,130,50,50))
    pygame.draw.rect(screen,button, (50,200,170,50))
    pygame.draw.rect(screen,button, (280,200,170,50))
    pygame.draw.rect(screen,black , (45,495,410,60))
    pygame.draw.rect(screen,button, (50,500,400,50))

    screen.blit(text_min,(10,45))
    screen.blit(text_min,(420,45))

    screen.blit(text_sec,(10,125))
    screen.blit(text_sec,(420,125))

    screen.blit(text_cong,(110,45))
    screen.blit(text_cong,(110,125))

    screen.blit(text_tru,(365,45))
    screen.blit(text_tru,(365,125))

    screen.blit(text_start,(90,200))
    screen.blit(text_reset,(320,200))

    pygame.draw.circle(screen, black, (250,380),100)
    pygame.draw.circle(screen, button, (250,380),97)
    pygame.draw.circle(screen, black, (250,380),5)

    text_time = font1.render(str(mins) + ':' + str(secs),True,font_color)
    screen.blit(text_time,(155,50))
    
    if total != 0:
        pygame.draw.rect(screen ,red ,(50,500,int(400 * (total_secs / total)),50))
    
    x_sec = 250 + 90 * math.sin(6*secs*math.pi/180)
    y_sec = 380 - 90 * math.cos(6*secs*math.pi/180)
    pygame.draw.line(screen, black, (250,380),(int(x_sec),int(y_sec)))

    x_min = 250 + 50 * math.sin(6*mins*math.pi/180)
    y_min = 380 - 50 * math.cos(6*mins*math.pi/180)
    pygame.draw.line(screen, blue, (250,380),(int(x_min),int(y_min)))


    pygame.display.flip()
    clock.tick(60)
pygame.quit()