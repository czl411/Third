import pygame
import sys
from pygame.locals import *
import Join_Room_Page
import Creat_Room_Page
import Login_page

class Main_page_C():
    def __init__(self,mordern,header,name):
        self.Black = (0,0,0)
        self.size = 1012, 596
        self.bg_imag = "source/background/Back_Ground3~1.png"
        self.GB_img = "source/background/Icon_get_back~1.png"
        self.SET_img = "source/background/Icon_Setting~1.png"
        self.header=header
        self.mordern = mordern
        self.name =name
        self.select = 0
        self.creat_page()


    def creat_page(self):
        pygame.init()
        self.fontObj = pygame.font.Font("source/word_type/word3.TTF", 18)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.mordern)
        self.background = pygame.image.load(self.bg_imag).convert_alpha()
        self.GBIMG = pygame.image.load(self.GB_img).convert_alpha()
        self.SEIMG = pygame.image.load(self.SET_img).convert_alpha()
        self.clock = pygame.time.Clock()
        while(1):
            self.screen.blit(self.background,(-22,0))
            self.screen.blit(self.GBIMG,(27, 15))
            self.screen.blit(self.fontObj.render("加入房间",
                                                 False, self.Black), (310, 315))
            self.screen.blit(self.fontObj.render("创建房间",
                                                 False, self.Black), (610, 315))
            pygame.draw.rect(self.screen, self.Black, [310, 315, 72, 18], 1)  # 加入犯贱
            pygame.draw.rect(self.screen, self.Black, [610, 315, 72, 18], 1)  # 创建房间
            pygame.draw.rect(self.screen, self.Black, [40, 25, 80, 30], 1)  # fanhui
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                buttons = pygame.mouse.get_pressed()  # 存鼠标状态
                x, y = pygame.mouse.get_pos()
                if 310 < x <382 and 315 < y < 333 and\
                    event.type == MOUSEBUTTONDOWN:
                    self.select = 1
                    break
                if 610 < x < 682 and 315 < y < 333 and \
                    event.type == MOUSEBUTTONDOWN:
                    self.select = 2
                    break
                if 40 < x < 120 and 25 < y < 55 and \
                    event.type == MOUSEBUTTONDOWN:
                    self.select = 3
                    break
            if self.select != 0:
                break
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()
        if self.select == 1:
            Join_Room_Page.Join_page(self.header, self.name)
        elif self.select == 2:
            Creat_Room_Page.Creat_Room_page(self.header, self.name)
        elif self.select == 3:
            Login_page.loginpage()


