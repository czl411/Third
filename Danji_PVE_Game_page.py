import pygame
import sys
from pygame.locals import *
import Danji_Game_Part
import json
from game import *
import os

class Game_page_C():
    def __init__(self,mordern):
        self.load()
        self.Black = (0,0,0)
        self.size = 1012, 596
        self.bg_imag = "source/background/Back_Ground3~1.png"
        self.GB_img = "source/background/Icon_get_back~1.png"
        self.SET_img = "source/background/Icon_Setting~1.png"
        self.Game = Game_Rule()
        self.P = []
        self.P.append(Player("P1"))
        self.P.append(Player("AI"))
        self.Cards = Card_zu()
        self.Place_Area = Placement_Area()
        self.name = mordern

        self.HeiTao_center = (110 * 2 + 70 ) / 2 , ( 415 * 2 + 100 ) / 2
        self.HongXin_center = ( 186 * 2+ 70 ) / 2, ( 415 * 2 + 100 ) / 2
        self.FangKuai_center = (262 * 2 + 70) / 2, (415 * 2 + 100) / 2
        self.MeiHua_center = (338 * 2 + 70) / 2, (415 * 2 + 100) / 2

        self.HeiTao_center_2 = ((947-110) * 2 + 70) / 2, ((596 - 442) * 2 + 100) / 2


        self.qipai_center = (535 * 2 + 80) / 2, (280 * 2 + 110) / 2
        self.cards_center = (405 * 2 + 80) / 2, (280 * 2 + 110) / 2

        self.creat_page()
        self.Game_over()

    def load(self):
        json_path = 'image.json'
        f = open(json_path, 'r', encoding='utf-8')
        self.img_url_dict = json.load(f)
        f.close()

    def page_loading(self):
        if len(self.P[0].S) > 0:
            self.card1 = self.img_url_dict[self.P[0].S[len(self.P[0].S) - 1]]
            self.cards1 = pygame.image.load(self.card1).convert_alpha()
            self.card1_rect = self.cards1.get_rect()
            self.card1_rect.center = self.HeiTao_center
        if len(self.P[0].H) > 0:
            self.card2 = self.img_url_dict[self.P[0].H[len(self.P[0].H) - 1]]
            self.cards2 = pygame.image.load(self.card2).convert_alpha()
            self.card2_rect = self.cards2.get_rect()
            self.card2_rect.center = self.HongXin_center
        if len(self.P[0].D) > 0:
            self.card3 = self.img_url_dict[self.P[0].D[len(self.P[0].D) - 1]]
            self.cards3 = pygame.image.load(self.card3).convert_alpha()
            self.card3_rect = self.cards3.get_rect()
            self.card3_rect.center = self.FangKuai_center
        if len(self.P[0].C) > 0:
            self.card4 = self.img_url_dict[self.P[0].C[len(self.P[0].C) - 1]]
            self.cards4 = pygame.image.load(self.card4).convert_alpha()
            self.card4_rect = self.cards4.get_rect()
            self.card4_rect.center = self.MeiHua_center

        if self.P[1].sum > 0:
            self.card5 = self.img_url_dict[' ']
            self.cards5 = pygame.image.load(self.card5).convert_alpha()
            self.card5_rect = self.cards5.get_rect()
            self.card5_rect.center = self.HeiTao_center_2

        if len(self.Place_Area.card):
            card = self.Place_Area.card[len(self.Place_Area.card)-1]
            self.card9 = self.img_url_dict.get(card,"source/card/SA.png")
            self.cards9 = pygame.image.load(self.card9).convert_alpha()
            self.card9_rect = self.cards9.get_rect()
            self.card9_rect.center = self.qipai_center

    def creat_page(self):
        pygame.init()
        self.fontObj = pygame.font.Font("source/word_type/word3.TTF", 18)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)
        self.background = pygame.image.load(self.bg_imag).convert_alpha()
        self.GBIMG = pygame.image.load(self.GB_img).convert_alpha()
        self.SEIMG = pygame.image.load(self.SET_img).convert_alpha()
        self.clock = pygame.time.Clock()
        self.who = 0
        while(self.Cards.sum):
            self.page_loading()
            self.screen.blit(self.background, (-22, 0))
            self.screen.blit(self.GBIMG, (27, 15))
            self.screen.blit(self.SEIMG, (117, 15))
            if len(self.P[0].S):
                self.screen.blit(self.cards1, self.card1_rect)
            if len(self.P[0].H):
                self.screen.blit(self.cards2, self.card2_rect)
            if len(self.P[0].D):
                self.screen.blit(self.cards3, self.card3_rect)
            if len(self.P[0].C):
                self.screen.blit(self.cards4, self.card4_rect)

            if self.P[1].sum:
                self.screen.blit(self.cards5, self.card5_rect)

            if self.Place_Area.sum:
                self.screen.blit(self.cards9,self.card9_rect)

            self.screen.blit(self.fontObj.render(f"??????:{len(self.P[0].S)}",
                                                 False,self.Black),(110,515))
            self.screen.blit(self.fontObj.render(f"??????:{len(self.P[0].H)}",
                                                 False, self.Black), (186, 515))
            self.screen.blit(self.fontObj.render(f"??????:{len(self.P[0].D)}",
                                                 False, self.Black), (262, 515))
            self.screen.blit(self.fontObj.render(f"??????:{len(self.P[0].C)}",
                                                 False, self.Black), (338, 515))

            self.screen.blit(self.fontObj.render(f"AI:{self.P[1].sum}",
                                                 False, self.Black), (947-110, 596-442-20))


            self.screen.blit(self.fontObj.render(f"??????:{self.Place_Area.sum}",
                                                 False, self.Black), (535, 390))
            self.screen.blit(self.fontObj.render(f"??????:{self.Cards.sum}",
                                                 False, self.Black), (405, 260))
            self.screen.blit(self.fontObj.render(f"P{self.who}?????????",
                                                 False, self.Black), (150, 150))

            pygame.draw.rect(self.screen, self.Black, [110, 415, 70, 100], 1)   # P1??????
            pygame.draw.rect(self.screen, self.Black, [186, 415, 70, 100], 1)   # P1???
            pygame.draw.rect(self.screen, self.Black, [262, 415, 70, 100], 1)   # P1??????
            pygame.draw.rect(self.screen, self.Black, [338, 415, 70, 100], 1)   # P1??????
            pygame.draw.rect(self.screen, self.Black, [947-110, 596-442, 70, 100], 1)  # P2??????

            pygame.draw.rect(self.screen, self.Black, [40, 25, 80, 30], 1)  # fanhui
            pygame.draw.rect(self.screen, self.Black, [130, 25, 80, 30], 1)  # ??????
            pygame.draw.rect(self.screen, self.Black, [535, 280, 80, 110], 1)  # ??????
            pygame.draw.rect(self.screen, self.Black, [405, 280, 80, 110], 1)  # ??????

            self.status = 1
            while(self.status and self.who == 0):
                buttons = pygame.mouse.get_pressed()  # ???????????????
                x, y = pygame.mouse.get_pos()
                card = str()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                    if x >40 and x < 120 and y > 15 and y < 45 and\
                            event.type == MOUSEBUTTONDOWN:
                            pygame.quit()
                            Danji_Game_Part.danji_page()
                    if 110 < x < 180 and 415 < y < 515 and\
                            event.type == MOUSEBUTTONDOWN and len(self.P[0].S) > 0:
                        card = self.P[0].Knockout_S() #????????????
                    if 186< x < 256 and 415 < y < 515 and\
                            event.type == MOUSEBUTTONDOWN and len(self.P[0].H) > 0:
                        card = self.P[0].Knockout_H() #????????????
                    if 262 < x < 332 and 415 < y < 515 and\
                            event.type == MOUSEBUTTONDOWN and len(self.P[0].D) > 0:
                        card = self.P[0].Knockout_D()  #????????????
                    if 338 < x < 408 and 415 < y < 515 and\
                            event.type == MOUSEBUTTONDOWN and len(self.P[0].C) > 0:
                        card = self.P[0].Knockout_C() #????????????
                    if 405 < x < 405 + 80 and 280 < y < 280 + 110 and\
                            event.type == MOUSEBUTTONDOWN:
                        card = self.Cards.random_card()
                    if card:
                        self.Place_Area.Put_in(card)
                        self.status = 0
                pygame.display.update()

            while(self.status and self.who):
                buttons = pygame.mouse.get_pressed()  # ???????????????
                x, y = pygame.mouse.get_pos()
                card = str()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                    if x >40 and x < 120 and y > 15 and y < 45 and\
                            event.type == MOUSEBUTTONDOWN:
                            Danji_Game_Part.danji_page()

                    if 405 < x < 405 + 80 and 280 < y < 280 + 110 and\
                            event.type == MOUSEBUTTONDOWN:
                        card = self.Cards.random_card()
                    if card:
                        self.Place_Area.Put_in(card)
                        self.status = 0
                pygame.display.update()
            if len(self.Place_Area.card):
                print("Place_Area:",self.Place_Area.card)
            if self.Game.Whether_Eat_Cards(self.Place_Area):
                 self.P[self.who].Eat_Cards(self.Place_Area)

            self.who = (self.who+1)%2
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()

    def Game_over(self):
        pygame.init()
        pygame.display.set_caption("Game over")
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # ????????????
        screen = pygame.display.set_mode((500,240))
        background = pygame.image.load("source/background/????????????.gif").convert_alpha()
        clock = pygame.time.Clock()
        while(1):
            screen.blit(background, (0, 0))
            fontObj = pygame.font.Font("source/word_type/word3.TTF", 32)
            screen.blit(fontObj.render(f"P1:{self.P[0].sum}     P2:{self.P[1].sum}",
                                       False, self.Black), (130, 50))

            if self.P[0].sum < self.P[1].sum:
                screen.blit(fontObj.render("P1 WIN", False, self.Black), (200, 100))
            elif self.P[0].sum > self.P[1].sum:
                screen.blit(fontObj.render("AI WIN", False, self.Black), (200, 100))
            elif self.P[0].sum == self.P[1].sum:
                screen.blit(fontObj.render("??????", False, self.Black), (225, 100))
            fontObj = pygame.font.Font("source/word_type/word3.TTF", 24)
            screen.blit(fontObj.render("????????????        ????????????",
                                       False, self.Black), (130, 200))
            pygame.draw.rect(screen, self.Black, [130, 200, 24*4, 24], 1)
            pygame.draw.rect(screen, self.Black, [130+24*6.5, 200, 24*4, 24], 1)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                buttons = pygame.mouse.get_pressed()  # ???????????????
                x, y = pygame.mouse.get_pos()
                if 130 < x < 130 +24*4 and 200 < y < 200 +24 and \
                        event.type == MOUSEBUTTONDOWN:
                    pygame.quit()
                    Game_page_C('PVE')
                if 130+24*6.5 < x < 130 +24*10.5 and 200 < y < 200 +24 and \
                        event.type == MOUSEBUTTONDOWN:
                    pygame.quit()
                    Danji_Game_Part.danji_page()
            pygame.display.update()
            clock.tick(30)
