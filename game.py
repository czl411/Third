import random as r

class Card:                     #卡牌类
    def __init__(self,sum=0):
        self.sum = sum
        self.card = []

class Card_zu(Card):            #卡组类
    def __init__(self):
        super().__init__()
        self.sum=52                            #卡组卡牌数
        self.card=["SA","S2","S3","S4","S5","S6",'S7','S8','S9','S10','SJ','SQ','SK',
                   "HA","H2","H3","H4","H5","H6",'H7','H8','H9','H10','HJ','HQ','HK',
                   "CA","C2","C3","C4","C5","C6",'C7','C8','C9','C10','CJ','CQ','CK',
                   "DA","D2","D3","D4","D5","D6",'D7','D8','D9','D10','DJ','DQ','DK',]          #卡组组成

    def random_card(self):
        card = self.card.pop(r.randint(0,self.sum-1))
        self.sum = len(self.card)
        return card

class Placement_Area(Card):     #放置区类

    def Put_in(self,card):      #放入卡牌
        self.card.append(card)
        self.sum = len(self.card)

    def Empty_Card(self):       #放置区清零
        self.card.clear()
        self.sum=len(self.card)

class Player(Card):             #玩家类
    def __init__(self,name):
        super(Player, self).__init__()
        self.name=name
        self.S = []
        self.H = []
        self.D = []
        self.C = []

    def Knockout_S(self):         #打出S手牌
        Brand = len(self.S)
        return self.S.pop(Brand-1)
    def Knockout_H(self):         #打出H手牌
        Brand = len(self.H)
        return self.H.pop(Brand-1)
    def Knockout_D(self):         #打出D手牌
        Brand = len(self.D)
        return self.D.pop(Brand-1)
    def Knockout_C(self):         #打出C手牌
        Brand = len(self.C)
        return self.C.pop(Brand-1)

    def Touch_Card(self,Card_Group):#摸牌
        get_card = Card_Group.random_card()
        return get_card

    def Eat_Cards(self,Place_Area):#吃牌
        for card in Place_Area.card:
            if card[0]=='S':
                self.S.append(card)
            elif card[0]=='H':
                self.H.append(card)
            elif card[0]=='D':
                self.D.append(card)
            elif card[0]=='C':
                self.C.append(card)
        Place_Area.Empty_Card()
        self.sum = len(self.S)+len(self.H)+len(self.D)+len(self.C)

class Game_Rule:                    #游戏规则类
    def __init__(self):
        self.Game_Start = 1
        self.Gameing = 0
    def Whether_Eat_Cards(self,Place_Area): #判断是否吃牌
        if Place_Area.sum >= 2:
            if Place_Area.card[Place_Area.sum-2][0] == Place_Area.card[Place_Area.sum-1][0]:
                return 1
        return 0

# def Put_Place_Area(Place_Area,Game,card,who):   #放入放置区，并判断是否执行吃牌
#     if Place_Area.sum:  # 放置区不为空
#         if Game.Whether_Eat_Cards(card, Place_Area):  # 判断是否吃牌
#             Place_Area.Put_in(card)  # 先放入
#             P[who].Eat_Cards(Place_Area)  # P[who]吃牌
#         else:
#             Place_Area.Put_in(card)  # 放入放置区
#     else:
#         Place_Area.Put_in(card)  # 放入放置区

#
# '''
# 初始化，加载游戏内容
# '''
# Game = Game_Rule()
# P = []
# P.append(Player("陈志良"))
# P.append(Player("李知恩"))
#
# Cards = Card_zu()
# print(Cards.sum)
# Place_Area = Placement_Area()
# who = 0
# while Cards.sum != 0:
#     if P[who].sum == 0:                      #手上没牌
#         #print("%s手上没牌！"%P[who].name)
#         card = P[who].Touch_Card(Cards)    #P1摸牌
#         print("%s摸到了"%P[who].name,card)
#         # print("卡组剩余：", Cards.sum)
#         # print(Cards.card)
#         Put_Place_Area(Place_Area, Game, card, who)
#     else:
#         print("%s的当前手牌："%P[who].name,end=' ')
#         for i in P[who].card:
#             print(i,end=' ')
#         # print("当前放置区的牌：",end=' ')
#         # for i in Place_Area.card:
#         #     print(i, end=' ')
#         print("\nA:打出手牌\nB:摸牌")
#         Operation = str(input('\n请输入要执行的操作:'))
#         if Operation == 'B':
#             card = P[who].Touch_Card(Cards)  # who摸牌
#             #print("卡组剩余：", Cards.sum)
#             Put_Place_Area(Place_Area,Game,card,who)
#         elif Operation == 'A':
#             card = P[who].Knockout()         #P[who]打出
#             Put_Place_Area(Place_Area,Game,card,who)
#         elif Operation == 'S':
#             break
#     print("卡组：%d"%Cards.sum)
#     print(Cards.card)
#     print("放堆：%d"%Place_Area.sum)
#     print(Place_Area.card)
#     print("1P:%d"%P[0].sum)
#     print(P[0].card)
#     print("2P：%d" %P[1].sum)
#     print(P[1].card)
#     who = (who+1)%2
