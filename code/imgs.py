import pygame, random
from os.path import join
from settings import Window_Height, Window_Width


# Fonts
main_font = pygame.font.Font(join('images', 'BankGothic Md BT.ttf'), 40)
big_font = pygame.font.Font(join('images', 'BankGothic Md BT.ttf'), 60)


# BGs
def random_mainBG():
    global BG_main
    
    ranbg_main = ['aces.png', 'dices.png', 'rolet.png', 'rolet2.png']
    
    BG_main = pygame.image.load(join('images', 'main', random.choice(ranbg_main))).convert_alpha()
    BG_main = pygame.transform.scale(BG_main, (Window_Width, Window_Height))
    
    return BG_main

BG_settings = pygame.image.load(join('images', 'settingsbg.png')).convert_alpha()
BG_settings = pygame.transform.scale(BG_settings, (Window_Width, Window_Height))

BG_lucky_dices = pygame.image.load(join('images', 'main', 'dices.png')).convert_alpha()
BG_lucky_dices = pygame.transform.scale(BG_lucky_dices, (Window_Width, Window_Height))


# Buttons
## small: 300 x 100
s_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
s_button_width, s_button_height = 300, 100
s_button_surface = pygame.transform.scale(s_button_surface, (s_button_width, s_button_height))

## medium: 450 x 150
m_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
m_button_width, m_button_height = 450, 150
m_button_surface = pygame.transform.scale(m_button_surface, (m_button_width, m_button_height))






