
import pygame, random, json, sys
from os.path import join


#general setup
pygame.init()
running = True
clock = pygame.time.Clock()
current_state = 'main_menu'


# Resizable Screen
from settings import update_data, Window_Width, Window_Height
BASE_WIDTH, BASE_HEIGHT = 1280, 720

base_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
display_surface = pygame.display.set_mode((Window_Width, Window_Height), pygame.RESIZABLE)

pygame.display.set_caption('Juluma Royale')
icon_surface = pygame.image.load(join('images','logos', 'monogramm_black.png')).convert_alpha()
pygame.display.set_icon(icon_surface)


# images / buttons / fonts / Classes
from imgs import *
BG_main = random_mainBG()


# Chip System
def load_chipcount():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data.get('chips', 1000)
    except (FileNotFoundError, json.JSONDecodeError):
        return 1000

def win_chips(amount):
    global chip_count
    chip_count += amount
    update_data(chips = chip_count)

def lose_chips(amount):
    global chip_count
    chip_count = max(0, chip_count - amount)
    update_data(chips = chip_count)

def chip_reset():
    global chip_count
    chip_count = 1000
    
    ok = Button(s_button_surface, Window_Width/2, Window_Height - 300, 'Thanks', back_to_menu)
    
    text_surf = main_font.render('Chips got restocked', True, 'gold')
    text_rect = text_surf.get_rect(center=(Window_Width // 2, Window_Height - 500))
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_data(chip_count)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = get_scaled_mouse_pos()
                ok.checkForInput(pygame.mouse.get_pos())
                waiting = False
        
        base_surface.fill((0,0,0))
        mx, my = get_scaled_mouse_pos()
        ok.changeColor(pygame.mouse.get_pos())
        ok.update(base_surface)
        display_surface.blit(text_surf, text_rect)
        
        draw_scaled()
        clock.tick(60)

def draw_chip_counter():
    chip_text = big_font.render(f'chips: {chip_count}', True, 'white')
    base_surface.blit(chip_text, (100,50))

chip_count = load_chipcount()


# get scaled mouse position
def get_scaled_mouse_pos():
    mx, my = pygame.mouse.get_pos()
    window_w, window_h = display_surface.get_size()
    scale_x = BASE_WIDTH / window_w
    scale_y = BASE_HEIGHT / window_h
    return mx * scale_x, my * scale_y

# Draw scaled output
def draw_scaled():
    window_w, window_h = display_surface.get_size()
    scaled_surface = pygame.transform.smoothscale(base_surface, (window_w, window_h))
    display_surface.blit(scaled_surface, (0, 0))
    pygame.display.update()


# state functions
def quit_game():
    global running
    running = False

def back_to_menu():
    global current_state
    current_state = 'main_menu'
    global BG_main
    BG_main = random_mainBG()

def open_settings():
    global current_state
    current_state = 'settings'

def go_lucky_dices():
    global current_state
    current_state = 'lucky_dices'


# Menu functions
def gameclose_buttoninput(buttons):
    global display_surface, Window_Width, Window_Height
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.VIDEORESIZE:
            Window_Width, Window_Height = event.w, event.h
            display_surface = pygame.display.set_mode((Window_Width, Window_Height), pygame.RESIZABLE)
            update_data(Window_Width=Window_Width, Window_Height=Window_Height)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = get_scaled_mouse_pos()
            for button in buttons:
                button.checkForInput((mx, my))

def update_buttons(buttons, surface):
    mx, my = get_scaled_mouse_pos()
    for button in buttons:
        button.changeColor((mx, my))
        button.update(surface)


def main_menu():
    quit_button = Button(s_button_surface, 200, 650, 'Quit', quit_game)
    settings_button = Button(s_button_surface, 500, 650, 'Settings', open_settings)
    lucky_dices_button = Button(m_button_surface, 350, 300, 'Lucky Dice', go_lucky_dices)
    
    buttons = [quit_button, settings_button, lucky_dices_button]
    
    
    while current_state == 'main_menu' and running:
        gameclose_buttoninput(buttons)
        base_surface.fill((0, 0, 0))
        base_surface.blit(BG_main, (0,0))
        draw_chip_counter()
        
        update_buttons(buttons, base_surface)
        draw_scaled()
        
        clock.tick(60)
        
        if current_state != 'main_menu' or not running:
            break

def settings_menu():
    back_button = Button(s_button_surface, 200, 650, 'Back', back_to_menu)
    buttons = [back_button]
    
    while current_state == 'settings' and running:
        gameclose_buttoninput(buttons)
        
        base_surface.blit(BG_settings, (0,0))
        update_buttons(buttons, base_surface)
        draw_scaled()
        
        clock.tick(60)
        
        if current_state != 'settings' or not running:
            break

def lucky_dices():
    
    dicean_on = False
    def play():
        nonlocal dicean_on, time_running, last_frame_change, final_frame_index
        time_running = 0
        last_frame_change = 0
        final_frame_index = None
        dicean_on = True
    
    back_button = Button(s_button_surface, 200, 650, 'Back', back_to_menu)
    play_button = Button(s_button_surface, 200, 500, 'Play', play)
    b_1 = Button(mi_button_surface, 150, 200, '1')
    b_2 = Button(mi_button_surface, 250, 200, '2')
    b_3 = Button(mi_button_surface, 150, 300, '3')
    b_4 = Button(mi_button_surface, 250, 300, '4')
    b_5 = Button(mi_button_surface, 150, 400, '5')
    b_6 = Button(mi_button_surface, 250, 400, '6')
    buttons = [back_button, play_button, b_1, b_2, b_3, b_4, b_5, b_6]
    
    
    # surface for animation
    dicesurf_scale = 250
    dicesurf = pygame.Surface((dicesurf_scale, dicesurf_scale), pygame.SRCALPHA)
    
    # Frames
    dices_1_6 = [
        pygame.transform.smoothscale(pygame.image.load(join('images','dices','dice1.png')).convert_alpha(), (dicesurf_scale,dicesurf_scale)),
        pygame.transform.smoothscale(pygame.image.load(join('images','dices','dice2.png')).convert_alpha(), (dicesurf_scale,dicesurf_scale)),
        pygame.transform.smoothscale(pygame.image.load(join('images','dices','dice3.png')).convert_alpha(), (dicesurf_scale,dicesurf_scale)),
        pygame.transform.smoothscale(pygame.image.load(join('images','dices','dice4.png')).convert_alpha(), (dicesurf_scale,dicesurf_scale)),
        pygame.transform.smoothscale(pygame.image.load(join('images','dices','dice5.png')).convert_alpha(), (dicesurf_scale,dicesurf_scale)),
        pygame.transform.smoothscale(pygame.image.load(join('images','dices','dice6.png')).convert_alpha(), (dicesurf_scale,dicesurf_scale)),
    ]
    
    # timer for frame switch
    frame_time = 100
    last_frame_change = 0
    dicean_duration = 2000
    time_running = 0
    current_frame = random.choice(dices_1_6)
    final_frame_index = None                # index always -1 of rolled number
    
    
    
    while current_state == 'lucky_dices' and running:
        delta_time = clock.tick(60)
        gameclose_buttoninput(buttons)
        
        
        # Dice Animation
        if dicean_on == True:
            last_frame_change += delta_time
            time_running += delta_time
            
            if last_frame_change >= frame_time:
                last_frame_change = 0
                current_frame = random.choice(dices_1_6)
            
            if time_running >= dicean_duration:
                dicean_on = False
                final_frame_index = dices_1_6.index(current_frame)
                print('final frame index:', final_frame_index)
        
        dicesurf.fill((0,0,0,0))
        dicesurf.blit(current_frame, (0,0))
        
        
        
        
        
        
        
        base_surface.blit(BG_lucky_dices, (0,0))
        base_surface.blit(dicesurf,(450,400))
        draw_chip_counter()
        update_buttons(buttons, base_surface)
        draw_scaled()
        
        
        clock.tick(60)
        
        if current_state != 'lucky_dices' or not running:
            break


# main loop
states = {
    'main_menu': main_menu,
    "settings": settings_menu,
    "lucky_dices": lucky_dices}

while running:
    if chip_count < 1000:
        chip_reset()
    
    else:
        states[current_state]()



update_data(chips = chip_count)
pygame.quit()