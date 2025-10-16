import pygame, random, json
from os.path import join


#general setup
pygame.init()
running = True
clock = pygame.time.Clock()
main_font = pygame.font.Font(join('images', 'BankGothic Md BT.ttf'), 40)

Window_Width, Window_Height = 1280, 720
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Juluma Royale')
icon_surface = pygame.image.load(join('images','logos', 'monogramm_black.png')).convert_alpha()
pygame.display.set_icon(icon_surface)

current_state = 'main_menu'


# backgrounds
ranbg_main = ['aces.png', 'dices.png', 'rolet.png', 'rolet2.png']
BG_main = pygame.image.load(join('images', 'main', random.choice(ranbg_main))).convert_alpha()
BG_main = pygame.transform.scale(BG_main, (Window_Width, Window_Height))

BG_settings = pygame.image.load(join('images', 'settingsbg.png')).convert_alpha()
BG_settings = pygame.transform.scale(BG_settings, (Window_Width, Window_Height))

BG_lucky_dices = pygame.Surface((Window_Width, Window_Height))
BG_lucky_dices.fill((100, 50, 20))


# Button picture
button_surface = pygame.image.load(join('images', 'buttonbg.png')).convert_alpha()
button_width, button_height = 300, 100
button_surface = pygame.transform.scale(button_surface, (button_width, button_height))


# Chip Counter

def load_data():
    try:
        with open('save_data.json', 'r') as file:
            data = json.load(file)
            return data.get('chips', 1000)
    except FileNotFoundError:
        return 1000

def save_data(chips):
    with open('save_data.json', 'w') as file:
        json.dump({'chips': chips}, file)

def win_chips(amount):
    global chip_count
    chip_count += amount
    save_data(chip_count)

def lose_chips(amount):
    global chip_count
    chip_count = max(0, chip_count - amount)
    save_data(chip_count)

chip_count = load_data()


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
    
    def update(self):
        display_surface.blit(self.image, self.rect)
        display_surface.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            if self.on_click:
                self.on_click()
    
    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = main_font.render(self.text_input, True, 'gold')
        else:
            self.text = main_font.render(self.text_input, True, 'white')


# state functions
def quit_game():
    global running
    running = False

def back_to_menu():
    global current_state
    current_state = 'main_menu'

def open_settings():
    global current_state
    current_state = 'settings'


def go_lucky_dices():
    global current_state
    current_state = 'lucky_dices'


# Menu functions
def main_menu():
    quit_button = Button(button_surface, 200, 650, 'Quit', quit_game)
    settings_button = Button(button_surface, 500, 650, 'Settings', open_settings)
    buttons = [quit_button, settings_button]
    
    def draw_chip_counter():
        chip_text = main_font.render(f'chips: {chip_count}', True, 'white')
        display_surface.blit(chip_text, (50,50))
    
    while current_state == 'main_menu' and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.checkForInput(pygame.mouse.get_pos()) 
        
        display_surface.blit(BG_main, (0,0))
        
        draw_chip_counter()
        
        for button in buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update()
        
        pygame.display.update()
        clock.tick(60)

def settings_menu():
    back_button = Button(button_surface, 200, 650, 'Back', back_to_menu)
    buttons = [back_button]
    
    while current_state == 'settings' and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.checkForInput(pygame.mouse.get_pos())
        
        display_surface.blit(BG_settings, (0,0))
        for button in buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update()
        
        pygame.display.update()
        clock.tick(60)


def lucky_dices():
    back_button = Button(button_surface, 100 ,200, 'Back', back_to_menu)
    buttons = [back_button]
    
    while current_state == 'lucky_dices' and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.checkForInput(pygame.mouse.get_pos())
        
        display_surface.blit(BG_lucky_dices, (0,0))
        for button in buttons:
            button.changeColor(pygame.mouse.get_pos())
            button.update()
        
        pygame.display.update()
        clock.tick(60)

# main loop
while running:
    if current_state == 'main_menu':
        main_menu()
    elif current_state == 'settings':
        settings_menu()
    elif current_state == 'lucky_dices':
        lucky_dices()


save_data(chip_count)
pygame.quit()