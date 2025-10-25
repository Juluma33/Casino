import pygame, random
from os.path import join

Window_Width, Window_Height = 1280, 720

# BGs
ranbg_main = ['aces.png', 'dices.png', 'rolet.png', 'rolet2.png']
BG_main = pygame.image.load(join('images', 'main', random.choice(ranbg_main))).convert_alpha()
BG_main = pygame.transform.scale(BG_main, (Window_Width, Window_Height))

BG_settings = pygame.image.load(join('images', 'settingsbg.png')).convert_alpha()
BG_settings = pygame.transform.scale(BG_settings, (Window_Width, Window_Height))

BG_lucky_dices = pygame.Surface((Window_Width, Window_Height))
BG_lucky_dices.fill((100, 50, 20))




#Buttons

## small: 300 x 100
s_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
s_button_width, s_button_height = 300, 100
s_button_surface = pygame.transform.scale(s_button_surface, (s_button_width, s_button_height))

## medium: 400 x 150
m_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
m_button_width, m_button_height = 300, 100
m_button_surface = pygame.transform.scale(m_button_surface, (m_button_width, m_button_height))


# Dice images
dices_images = {i: pygame.image.load(join('images', 'dices', f'dice{i}.png')).convert_alpha() for i in range(1, 7)}