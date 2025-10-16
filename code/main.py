import pygame, random
from os.path import join

#general setup
pygame.init()
running = True
clock = pygame.time.Clock()
main_font = pygame.font.SysFont('cambria', 20)

Window_Width, Window_Height = 1280, 720
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Juluma Royale')
icon_surface = pygame.image.load(join('images','logos', 'monogramm_black.png')).convert_alpha()
pygame.display.set_icon(icon_surface)


class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, 'white')
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
    
    def update(self):
        display_surface.blit(self.image, self.rect)
        display_surface.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print('Button Press!')
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, 'gold')
        else:
            self.text = main_font.render(self.text_input, True, 'white')


# main background
ranbg_main = ['aces.png', 'dices.png', 'rolet.png', 'rolet2.png']
BG_main = pygame.image.load(join('images', 'main', random.choice(ranbg_main)))
BG_main = pygame.transform.scale(BG_main, (Window_Width, Window_Height))

# Import
button_surface = pygame.image.load(join('images', 'buttonbg.png'))
button_surface = pygame.transform.scale(button_surface, (100, 200))






def main_menu():
    global running
    
    quit_button = Button(button_surface, 100, 200, 'Test')
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                quit_button.checkForInput(pygame.mouse.get_pos()) 
        
        # display
        display_surface.blit(BG_main)
        
        quit_button.update()
        quit_button.changeColor(pygame.mouse.get_pos())
        
        
        pygame.display.update()

main_menu()


pygame.quit()