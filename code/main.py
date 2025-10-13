import pygame, random
from os.path import join


#general setup
pygame.init()
running = True
clock = pygame.time.Clock()

from settings import *
Window_Width, Window_Height = 1280, 720
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Juluma Royale')
icon_surface = pygame.image.load(join('images','logos', 'monogramm_black.png')).convert_alpha()
pygame.display.set_icon(icon_surface)

# main background
ranbg_main = 'aces.png'
BG_main = pygame.image.load(join('images', 'main', 'aces.png')).convert_alpha()

while running:
    
    display_surface.blit(BG_main)
    
    
    #framerate
    dt = clock.tick() / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    
    
    
    pygame.display.update()




pygame.QUIT()