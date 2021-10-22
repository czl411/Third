import pygame
from pygame.locals import *
import main_page
import sys

class welcome_page():
    def __init__(self):
        self.size = 1012,596
        self.bg_imag = "source/background/Back_Ground4~1.png"
        self.SG_imag = "source/background/Start_Game~1.png"
        self.Logo_img = "source/background/Logo_Big~1.png"
        self.creat_page()

    def creat_page(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("猪尾巴")
        self.background = pygame.image.load(self.bg_imag).convert_alpha()
        self.Start = pygame.image.load(self.SG_imag).convert_alpha()
        self.Logo = pygame.image.load(self.Logo_img).convert_alpha()
        self.clock = pygame.time.Clock()
        while(1):
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Logo,(50,0))
            self.screen.blit(self.Start,(100, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    main_page.main_page()
            pygame.display.update()
            self.clock.tick(30)
            
# welcome_page()