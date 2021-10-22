class Card:                     #卡牌类
    def __init__(self,sum=0):
        self.sum = sum
        self.card = []

class Card_zu(Card):            #卡组类
    def __init__(self):
        super().__init__()
        self.sum=52                                                                             #卡组卡牌数
        self.card=['SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
                   'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK',
                   'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
                   'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',]           #卡组组成

    def Updata_Card_zu(self,card):                                                               #更新卡组
        if card in self.card:
            self.card.pop(self.card.index(card))
            self.sum = self.sum-1

class Placement_Area(Card):                                                                     #放置区类

    def Update(self,card):                                                                      #放入卡牌
        if card not in self.card:
            self.card.append(card)
            self.sum = self.sum+1

    def Put_in(self,card):
        self.card.append(card)
        self.sum = self.sum + 1

    def  Whether_Eat_Cards(self):                                                               #判断是否吃牌
        if self.sum>=2:
            return self.card[self.sum-1][0]==self.card[self.sum-2][0]
        else:
            return False

    def Empty_Card(self):                                                                       #放置区清零
        self.card.clear()
        self.sum=0

class Player(Card):                                                                             #玩家类
    def __init__(self,name):
        super(Player, self).__init__()
        self.name=name
        self.S = []
        self.H = []
        self.D = []
        self.C = []

    def Update_Player_Card(self,Card):
        self.sum = len(self.card)
        if Card in self.card:
            self.card.pop(self.card.index(Card))
            self.sum=self.sum-1

    def Knockout_S(self):  # 打出S手牌
        Brand = len(self.S)
        return self.S.pop(Brand - 1)

    def Knockout_H(self):  # 打出H手牌
        Brand = len(self.H)
        return self.H.pop(Brand - 1)

    def Knockout_D(self):  # 打出D手牌
        Brand = len(self.D)
        return self.D.pop(Brand - 1)

    def Knockout_C(self):  # 打出C手牌
        Brand = len(self.C)
        return self.C.pop(Brand - 1)

    def Eat_Cards(self,Place_Area):#吃牌
        for card in Place_Area.card:
            self.card.append(card)
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
        self.sum = len(self.card)



