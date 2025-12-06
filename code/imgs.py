import pygame, random
from os.path import join
from settings import Window_Height, Window_Width


# class
class Button():
    def __init__(self, image, x_pos, y_pos, text_input, on_click=None):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, 'white')
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
        self.on_click = on_click
    
    def update(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            if self.on_click:
                self.on_click()
    
    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = main_font.render(self.text_input, True, 'gold')
        else:
            self.text = main_font.render(self.text_input, True, 'white')



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
## miniscular: 60 x 80
mi_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
mi_button_width, mi_button_height = 60, 80
mi_button_surface = pygame.transform.scale(mi_button_surface, (mi_button_width, mi_button_height))

## stretched miniscular: 200 x 80
st_mi_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
st_mi_button_width, st_mi_button_height = 60, 80
st_mi_button_surface = pygame.transform.scale(st_mi_button_surface, (st_mi_button_width, st_mi_button_height))

## small: 300 x 100
s_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
s_button_width, s_button_height = 300, 100
s_button_surface = pygame.transform.scale(s_button_surface, (s_button_width, s_button_height))

## medium: 450 x 150
m_button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
m_button_width, m_button_height = 450, 150
m_button_surface = pygame.transform.scale(m_button_surface, (m_button_width, m_button_height))





