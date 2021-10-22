import time
import pygame
import sys
from pygame.locals import *
import json

import Online_game
from Online_game import *
import os
import Online_sort_part
import LianJi_main_page
class Game_page_C():
    def __init__(self,mordern, uuid, name, header,who):
        self.load()
        self.Black = (0,0,0)
        self.size = 1012, 596
        self.bg_imag = "source/background/Back_Ground3~1.png"
        self.GB_img = "source/background/Icon_get_back~1.png"
        self.SET_img = "source/background/Icon_Setting~1.png"

        self.P = []
        self.P.append(Player("P0"))
        self.P.append(Player("P1"))
        self.Cards = Card_zu()
        self.Place_Area = Placement_Area()
        self.mordern = mordern
        self.uuid = uuid
        self.name = name
        self.header = header

        self.HeiTao_center = (110 * 2 + 70 ) / 2 , ( 415 * 2 + 100 ) / 2
        self.HongXin_center = ( 186 * 2+ 70 ) / 2, ( 415 * 2 + 100 ) / 2
        self.FangKuai_center = (262 * 2 + 70) / 2, (415 * 2 + 100) / 2
        self.MeiHua_center = (338 * 2 + 70) / 2, (415 * 2 + 100) / 2

        self.HeiTao_center_2 = ((947-110) * 2 + 70) / 2, ((596 - 442) * 2 + 100) / 2

        self.qipai_center = (535 * 2 + 80) / 2, (280 * 2 + 110) / 2
        self.cards_center = (405 * 2 + 80) / 2, (280 * 2 + 110) / 2
        self.id = who
        self.creat_page()
        self.Game_over()

    def load(self):
        json_path = 'image.json'
        f = open(json_path, 'r', encoding='utf-8')
        self.img_url_dict = json.load(f)
        f.close()

    def page_loading(self):
        if len(self.P[self.id].S) > 0:
            self.card1 = self.img_url_dict[self.P[self.id].S[len(self.P[self.id].S) - 1]]
            self.cards1 = pygame.image.load(self.card1).convert_alpha()
            self.card1_rect = self.cards1.get_rect()
            self.card1_rect.center = self.HeiTao_center
        if len(self.P[self.id].H) > 0:
            self.card2 = self.img_url_dict[self.P[self.id].H[len(self.P[self.id].H) - 1]]
            self.cards2 = pygame.image.load(self.card2).convert_alpha()
            self.card2_rect = self.cards2.get_rect()
            self.card2_rect.center = self.HongXin_center
        if len(self.P[self.id].D) > 0:
            self.card3 = self.img_url_dict[self.P[self.id].D[len(self.P[self.id].D) - 1]]
            self.cards3 = pygame.image.load(self.card3).convert_alpha()
            self.card3_rect = self.cards3.get_rect()
            self.card3_rect.center = self.FangKuai_center
        if len(self.P[self.id].C) > 0:
            self.card4 = self.img_url_dict[self.P[self.id].C[len(self.P[self.id].C) - 1]]
            self.cards4 = pygame.image.load(self.card4).convert_alpha()
            self.card4_rect = self.cards4.get_rect()
            self.card4_rect.center = self.MeiHua_center

        if self.P[1-self.id].sum > 0:
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
        while(1):
            self.screen.blit(self.background, (-22, 0))
            self.screen.blit(self.GBIMG, (27, 15))
            pygame.draw.rect(self.screen, self.Black, [40, 25, 80, 30], 1)  # fanhui
            self.screen.blit(self.fontObj.render(f"等待玩家加入！",
                                                 False, self.Black), (500, 255))
            res = Online_sort_part.Get_Previous_operation(self.uuid,self.header)
            if res["code"] == 200:
                self.State_zh = res["data"]["your_turn"]
                self.TG_F = -1
                break
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(30)
        while(self.Cards.sum):
            res = Online_sort_part.Get_Previous_operation(self.uuid,self.header)
            if res["code"] != 200:
                break
            self.page_loading()
            self.screen.blit(self.background, (-22, 0))
            self.screen.blit(self.GBIMG, (27, 15))
            self.screen.blit(self.SEIMG, (117, 15))
            if len(self.P[self.id].S):
                self.screen.blit(self.cards1, self.card1_rect)
            if len(self.P[self.id].H):
                self.screen.blit(self.cards2, self.card2_rect)
            if len(self.P[self.id].D):
                self.screen.blit(self.cards3, self.card3_rect)
            if len(self.P[self.id].C):
                self.screen.blit(self.cards4, self.card4_rect)

            if self.P[1-self.id].sum:
                self.screen.blit(self.cards5, self.card5_rect)

            if self.Place_Area.sum:
                self.screen.blit(self.cards9,self.card9_rect)

            self.screen.blit(self.fontObj.render(f"黑桃:{len(self.P[self.id].S)}",
                                                 False,self.Black),(110,515))
            self.screen.blit(self.fontObj.render(f"红心:{len(self.P[self.id].H)}",
                                                 False, self.Black), (186, 515))
            self.screen.blit(self.fontObj.render(f"方块:{len(self.P[self.id].D)}",
                                                 False, self.Black), (262, 515))
            self.screen.blit(self.fontObj.render(f"梅花:{len(self.P[self.id].C)}",
                                                 False, self.Black), (338, 515))

            self.screen.blit(self.fontObj.render(f"对手:{self.P[1-self.id].sum}",
                                                 False, self.Black), (947-110, 596-442-20))

            self.screen.blit(self.fontObj.render(f"托管",
                                                 False, self.Black), (150, 350))
            self.screen.blit(self.fontObj.render(f"房间号:{self.uuid}",
                                                 False, self.Black), (100, 250))
            self.screen.blit(self.fontObj.render(f"弃牌:{self.Place_Area.sum}",
                                                 False, self.Black), (535, 390))
            self.screen.blit(self.fontObj.render(f"卡组:{self.Cards.sum}",
                                                 False, self.Black), (405, 260))
            # self.screen.blit(self.fontObj.render(f"P{self.who}的回合",
            #                                      False, self.Black), (150, 150))

            pygame.draw.rect(self.screen, self.Black, [110, 415, 70, 100], 1)   # P1黑桃
            pygame.draw.rect(self.screen, self.Black, [186, 415, 70, 100], 1)   # P1心
            pygame.draw.rect(self.screen, self.Black, [262, 415, 70, 100], 1)   # P1方块
            pygame.draw.rect(self.screen, self.Black, [338, 415, 70, 100], 1)   # P1梅花
            pygame.draw.rect(self.screen, self.Black, [947-110, 596-442, 70, 100], 1)  # P2黑桃
            pygame.draw.rect(self.screen, self.Black, [150, 350, 34, 18], 1)  #托管
            pygame.draw.rect(self.screen, self.Black, [40, 25, 80, 30], 1)  # fanhui
            pygame.draw.rect(self.screen, self.Black, [130, 25, 80, 30], 1)  # 设置
            pygame.draw.rect(self.screen, self.Black, [535, 280, 80, 110], 1)  # 弃牌
            pygame.draw.rect(self.screen, self.Black, [405, 280, 80, 110], 1)  # 卡组
            buttons = pygame.mouse.get_pressed()  # 存鼠标状态
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if 40 < x < 40+80 and 25 < y <55 and\
                        event.type == MOUSEBUTTONDOWN:
                    pygame.quit()
                    LianJi_main_page.Main_page_C("联机",self.header,self.name)
                if 130 < x < 130+80 and 25<y<25+30 and event.type==MOUSEBUTTONDOWN:
                    pass
            Last_operation = res["data"]["last_code"]
            Your_Turn = res["data"]["your_turn"]
            if self.State_zh != Your_Turn:
                self.State_zh = Your_Turn
                if len(Last_operation) > 0:
                    OP_type = Last_operation[2]
                    card = Last_operation[4:]
                    if Your_Turn:
                        self.Cards.Updata_Card_zu(card)
                        self.Place_Area.Put_in(card)
                    if OP_type ==1 :
                        self.P[1-self.id].Update_Player_Card(card)
                    if self.Place_Area.Whether_Eat_Cards():
                        self.P[1-self.id].Eat_Cards(self.Place_Area)
            if Your_Turn == True:
                self.operation = {
                    "type": 0
                }
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                    if 40 < x < 40 + 80 and 25 < y < 55 and \
                            event.type == MOUSEBUTTONDOWN:
                        pygame.quit()
                        LianJi_main_page.Main_page_C("联机", self.header, self.name)
                    if 130 < x < 130 + 80 and 25 < y < 25 + 30 \
                            and event.type == MOUSEBUTTONDOWN:
                        pass
                    if 110 < x <180 and 415 <y <515 and \
                            event.type == MOUSEBUTTONDOWN and len(self.P[self.id].S) > 0:
                        self.operation["type"] = 1
                        self.operation["card"] = self.P[self.id].Knockout_S()
                    if 186 < x <186+70 and 415 <y <515 and \
                            event.type == MOUSEBUTTONDOWN and len(self.P[self.id].H) > 0:
                        self.operation["type"] = 1
                        self.operation["card"] = self.P[self.id].Knockout_H()
                    if 262 < x <262+70 and 415 <y <515 and \
                            event.type == MOUSEBUTTONDOWN and len(self.P[self.id].D) > 0:
                        self.operation["type"] = 1
                        self.operation["card"] = self.P[self.id].Knockout_D()
                    if 338 < x <338+70 and 415 <y <515 and \
                            event.type == MOUSEBUTTONDOWN and len(self.P[self.id].C) > 0:
                        self.operation["type"] = 1
                        self.operation["card"] = self.P[self.id].Knockout_C()
                    if 405 < x <405+80 and 280 <y <280+110 and \
                            event.type == MOUSEBUTTONDOWN:
                        self.DO_OP(self.P[self.id])
            pygame.display.update()
            self.clock.tick(30)
        pygame.quit()

    def Game_over(self):
        res = Online_sort_part.Get_Match_info(self.uuid, self.header)
        if res["data"]["winner"] == self.id:
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
        return
        # pygame.init()
        # pygame.display.set_caption("Game over")
        # os.environ['SDL_VIDEO_CENTERED'] = '1'  # 居中显示
        # screen = pygame.display.set_mode((500,240))
        # background = pygame.image.load("source/background/登陆界面.gif").convert_alpha()
        # clock = pygame.time.Clock()
        # while(1):
        #     screen.blit(background, (0, 0))
        #     fontObj = pygame.font.Font("source/word_type/word3.TTF", 32)
        #     screen.blit(fontObj.render(f"ME:{self.P[self.id].sum}    "
        #                                f" HE:{self.P[1-self.id].sum}",
        #                                False, self.Black), (130, 50))
        #
        #     res = Online_sort_part.Get_Match_info(self.uuid,self.header)
        #     if res["data"]["winner"]==self.id:
        #         print("YOU WIN!")
        #     else:
        #         print("YOU LOSE!")
        #     fontObj = pygame.font.Font("source/word_type/word3.TTF", 24)
        #     screen.blit(fontObj.render("继续游戏        结束游戏",
        #                                False, self.Black), (130, 200))
        #     pygame.draw.rect(screen, self.Black, [130, 200, 24*4, 24], 1)
        #     pygame.draw.rect(screen, self.Black, [130+24*6.5, 200, 24*4, 24], 1)
        #     for event in pygame.event.get():
        #         if event.type == QUIT:
        #             sys.exit()
        #         buttons = pygame.mouse.get_pressed()  # 存鼠标状态
        #         x, y = pygame.mouse.get_pos()
        #     pygame.display.update()
        #     clock.tick(30)

    def DO_OP(self,P):
        res = Online_sort_part.Player_operation(self.uuid,self.header,self.operation)
        card = res["data"]["last_code"][4:]
        self.Place_Area.Put_in(card)
        self.Cards.Updata_Card_zu(card)
        if self.Place_Area.Whether_Eat_Cards():
            P.Eat_Cards(self.Place_Area)