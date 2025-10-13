import pygame
from os.path import join
from random import randint


#general setup
pygame.init()
running = True
clock = pygame.time.Clock()

from settings import *
pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Juluma Royale')
icon_surface = pygame.image.load(join('images','logos', 'monogramm_black.png')).convert_alpha()
pygame.display.set_icon(icon_surface)


while running:
    #framerate
    dt = clock.tick() / 1000
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    pygame.display.update()
