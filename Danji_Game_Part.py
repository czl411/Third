import pygame
import sys
from pygame.locals import *
import main_page
import Danji_PVP_Game_page
import Danji_PVE_Game_page
class danji_page():
    def __init__(self):
        self.Black = (0,0,0)
        self.size = 1012,596
        self.select = 0
        self.creat_page()


    def creat_page(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.image.load("source/background/Back_Ground1~1.png") \
            .convert_alpha()
        self.PVP = pygame.image.load("source/background/Button_PVP~1.png") \
            .convert_alpha()
        self.PVE = pygame.image.load("source/background/Button_PVE~1.png") \
            .convert_alpha()
        self.GBIMG = pygame.image.load("source/background/Icon_get_back~1.png") \
            .convert_alpha()
        self.SEIMG = pygame.image.load("source/background/Icon_Setting~1.png") \
            .convert_alpha()
        self.LIMG = pygame.image.load("source/background/Logo_Small~1.png") \
            .convert_alpha()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("猪尾巴")
        while(1):
            for event in pygame.event.get():
                self.screen.blit(self.background, (-20, 0))
                self.screen.blit(self.PVP, (100 + 107-20, 100))
                self.screen.blit(self.PVE, (450 + 107-20, 100))
                self.screen.blit(self.GBIMG, (47-20, 15))
                self.screen.blit(self.SEIMG, (137-20, 15))
                self.screen.blit(self.LIMG, (850-20, -30))

                pygame.draw.rect(self.screen, self.Black, [110 + 110-20, 125, 250, 375], 1)  # PVP
                pygame.draw.rect(self.screen, self.Black, [460 + 110-20, 125, 250, 375], 1)  # PVE
                pygame.draw.rect(self.screen, self.Black, [60-20, 25, 80, 30], 1)  # fanhui
                pygame.draw.rect(self.screen, self.Black, [150-20, 25, 80, 30], 1)  # 设置

                buttons = pygame.mouse.get_pressed()  # 存鼠标状态
                x, y = pygame.mouse.get_pos()
                if x > 60-20 and x < 140-20 and y > 25 and y < 55 and buttons[0] \
                        and event.type == MOUSEBUTTONDOWN:
                    self.select = 1
                    break
                if x > 200 and x < 450 and y > 125 and y < 500 and buttons[0] \
                        and event.type == MOUSEBUTTONDOWN:
                    self.select = 2
                    break
                if x > 550 and x < 800 and y > 125 and y < 500 and buttons[0] \
                        and event.type == MOUSEBUTTONDOWN:
                    self.select = 3
                    break
                if event.type == QUIT:
                    sys.exit()
            pygame.display.update()
            self.clock.tick(30)
            if self.select != 0:
                break
        pygame.quit()
        if self.select == 1:
            main_page.main_page()
        elif self.select == 2:
            Danji_PVP_Game_page.Game_page_C('PVP')
        elif self.select == 3:
            Danji_PVE_Game_page.Game_page_C('PVE')