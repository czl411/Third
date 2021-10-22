import pygame
import sys
from pygame.locals import *
from Login_page import *
import Danji_Game_Part

class main_page():
    def __init__(self):
        self.Black = (0,0,0)
        self.bgm_high = 0.5  # bgm声音大小
        self.sound_high = 0.4  # 特效声音大小
        self.size = 1012,596
        self.BGM_url = "source/BGM/b1.ogg"
        self.mouse_sound_url = "source/sound/mouse_click.wav"
        self.keyboard_sound_url = "source/sound/keyboard_click.wav"
        self.bg_imag = "source/background/Back_Ground1~1.png"
        self.About_img = "source/background/Button_AboutGame~1.png"
        self.Single_img = "source/background/Button_SingleMode~1.png"
        self.OL_img = "source/background/Button_OnlineMode~1.png"
        self.Q_img = "source/background/Button_QuitGame~1.png"
        self.MORE_img = "source/background/Button_MottoGame~1.png"
        self.GB_img = "source/background/Icon_get_back~1.png"
        self.LO_img = "source/background/Logo_Small~1.png"
        self.SET_img = "source/background/Icon_Setting~1.png"
        self.creat_page()

    def creat_page(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("猪尾巴")
        pygame.mixer.music.load(self.BGM_url)
        pygame.mixer.music.set_volume(self.bgm_high)
        pygame.mixer.music.play()
        self.mouse_sound = pygame.mixer.Sound(self.mouse_sound_url)
        self.mouse_sound.set_volume(self.sound_high)
        self.keyboard_sound = pygame.mixer.Sound(self.keyboard_sound_url)
        self.keyboard_sound.set_volume(self.sound_high)
        self.background = pygame.image.load(self.bg_imag).convert_alpha()
        self.ABIMG = pygame.image.load(self.About_img).convert_alpha()
        self.SIMG = pygame.image.load(self.Single_img).convert_alpha()
        self.OIMG = pygame.image.load(self.OL_img).convert_alpha()
        self.QIMG = pygame.image.load(self.Q_img).convert_alpha()
        self.MIMG = pygame.image.load(self.MORE_img).convert_alpha()
        self.GBIMG = pygame.image.load(self.GB_img).convert_alpha()
        self.SEIMG = pygame.image.load(self.SET_img).convert_alpha()
        self.LIMG = pygame.image.load(self.LO_img).convert_alpha()
        self.clock = pygame.time.Clock()
        while(1):
            self.screen.blit(self.background, (-20, 0))
            self.screen.blit(self.GBIMG, (47-20, 15))
            self.screen.blit(self.SEIMG, (137-20, 15))
            self.screen.blit(self.LIMG, (850-20, -30))
            self.screen.blit(self.SIMG, (295-20, 115))
            self.screen.blit(self.OIMG, (500-20, 165))
            self.screen.blit(self.QIMG, (715-20, 163))
            self.screen.blit(self.ABIMG, (500-20, 315))
            self.screen.blit(self.MIMG, (715-20, 313))

            pygame.draw.rect(self.screen, self.Black, [60-20, 25, 80, 30], 1)  # fanhui
            pygame.draw.rect(self.screen, self.Black, [150-20, 25, 80, 30], 1)  # set
            pygame.draw.rect(self.screen, self.Black, [330-20, 185, 200, 290], 1)  # danji
            pygame.draw.rect(self.screen, self.Black, [535-20, 185, 210, 140], 1)  # zaixian
            pygame.draw.rect(self.screen, self.Black, [535-20, 335, 210, 140], 1)  # guanyuyiouyxi
            pygame.draw.rect(self.screen, self.Black, [750-20, 185, 210, 140], 1)  # genduo
            pygame.draw.rect(self.screen, self.Black, [750-20, 335, 210, 140], 1)  # tuichuyouyxi
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    self.mouse_sound.play()
                buttons = pygame.mouse.get_pressed()  # 存鼠标状态
                x, y = pygame.mouse.get_pos()
                if event.type == QUIT:
                    sys.exit()
                if x > 60-20 and x < 140-20 and y > 25 and y < 55 and buttons[0] and \
                        event.type == MOUSEBUTTONDOWN:
                    sys.exit()
                if x > 150-20 and x < 230-20 and y > 25 and y < 55 and buttons[0] and \
                        event.type == MOUSEBUTTONDOWN:
                    print("设置")
                if x > 330-20 and x < 530-20 and y > 185 and y < 185 + 290 and buttons[0] and\
                        event.type == MOUSEBUTTONDOWN:
                    pygame.quit()
                    Danji_Game_Part.danji_page()
                if x > 535-20 and x < 745-20 and y > 185 and y < 185 + 140 and buttons[0] and\
                        event.type == MOUSEBUTTONDOWN:
                    pygame.quit()
                    loginpage()
                if x > 535-20 and x < 745-20 and y > 335 and y < 335 + 140 and buttons[0] and\
                        event.type == MOUSEBUTTONDOWN:
                    print("关于")
                if x > 750-20 and x < 960-20 and y > 185 and y < 185 + 140 and buttons[0] and\
                        event.type == MOUSEBUTTONDOWN:
                    sys.exit()
                if x > 750-20 and x < 960-20 and y > 335 and y < 335 + 140 and buttons[0] and\
                        event.type == MOUSEBUTTONDOWN:
                    print("更多")

                if event.type == KEYDOWN:
                    self.keyboard_sound.play()
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_UP:
                        self.bgm_high += 0.05
                    if event.key == K_DOWN:
                        self.bgm_high -= 0.05
                    if event.key == K_LEFT:
                        self.sound_high += 0.05
                    if event.key == K_RIGHT:
                        self.sound_high -= 0.05
                pygame.mixer.music.set_volume(self.bgm_high)
                self.mouse_sound.set_volume(self.sound_high)
                self.keyboard_sound.set_volume(self.sound_high)
            pygame.display.update()
            self.clock.tick(30)