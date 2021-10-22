import copy
import random
import random as r
import datetime
import time
import math
class Card:                     #卡牌类
    def __init__(self,sum=0):
        self.sum = sum
        self.card = []

class Card_zu(Card):            #卡组类
    def __init__(self):
        super().__init__()
        self.sum=52                            #卡组卡牌数
        self.card=['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
                   'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK',
                   'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
                   'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',]          #卡组组成

    def random_card(self):
        card = self.card.pop(r.randint(0,self.sum-1))
        self.sum -= 1
        return card

class Placement_Area(Card):     #放置区类

    def Put_in(self,card):      #放入卡牌
        self.card.append(card)
        self.sum=len(self.card)

    def Empty_Card(self):       #放置区清零
        self.card.clear()
        self.sum=len(self.card)

class Player(Card):             #玩家类
    def __init__(self,name):
        super(Player, self).__init__()
        self.name=name

    def Knockout(self):         #打出手牌
        self.sum -= 1
        print("当前手牌数为：%d"%len(self.card))
        for card in self.card:
            print(card,end=' ')
        Brand = int(input('\n请输入要打出的牌号:'))
        return self.card.pop(Brand-1)

    def Touch_Card(self,Card_Group):#摸牌
        get_card = Card_Group.random_card()
        return get_card

    def Eat_Cards(self,Place_Area):#吃牌
        #print(self.name,"吃牌")
        for card in Place_Area.card:
            self.card.append(card)
        Place_Area.Empty_Card()
        self.sum = len(self.card)

class Game_Rule:                    #游戏规则类
    def __init__(self):
        self.Game_Start = 1
        self.Gameing = 0
    def Whether_Eat_Cards(self,What_Card,Place_Area): #判断是否吃牌
        if Place_Area.sum:
            if What_Card[0] == Place_Area.card[Place_Area.sum-1][0]:
                return 1
        return 0

def Put_Place_Area(Place_Area,Game,card,who):   #放入放置区，并判断是否执行吃牌
    if Place_Area.sum:  # 放置区不为空
        if Game.Whether_Eat_Cards(card, Place_Area):  # 判断是否吃牌
            Place_Area.Put_in(card)  # 先放入
            P[who].Eat_Cards(Place_Area)  # P[who]吃牌
        else:
            Place_Area.Put_in(card)  # 放入放置区
    else:
        Place_Area.Put_in(card)  # 放入放置区


def Put_vir_area(Place_Area,Game,card,who,gamer):   #放入虚拟放置区，并判断是否执行吃牌
    if Place_Area.sum:  # 放置区不为空
        if Game.Whether_Eat_Cards(card, Place_Area):  # 判断是否吃牌
            Place_Area.Put_in(card)  # 先放入
            gamer[who].Eat_Cards(Place_Area)  # P[who]吃牌
        else:
            Place_Area.Put_in(card)  # 放入放置区
    else:
        Place_Area.Put_in(card)  # 放入放置区

def judge(Gamer, choice):
    every_card = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    color_c = 0
    color_d = 0
    color_h = 0
    color_s = 0
    for i in every_card:
        t = 'C' + i
        color_c = color_c + Gamer.card.count(t)
    for i in every_card:
        t = 'D' + i
        color_d = color_d + Gamer.card.count(t)
    for i in every_card:
        t = 'H' + i
        color_h = color_h + Gamer.card.count(t)
    for i in every_card:
        t = 'S' + i
        color_s = color_s + Gamer.card.count(t)
    if color_c == 0:
        choice.remove('C')
    if color_d == 0:
        choice.remove('D')
    if color_h == 0:
        choice.remove('H')
    if color_s == 0:
        choice.remove('S')

    return choice

'''
初始化，加载游戏内容
'''
Game = Game_Rule()
P = []
P.append(Player("陈志良"))
P.append(Player("李知恩"))


Cards = Card_zu()
print(Cards.sum)
Place_Area = Placement_Area()   # 放置区
who = 0
while Cards.sum != 0:  # Cards表示卡组的状态
    if who == 0:
        if P[who].sum == 0:                      #手上没牌
            card = P[who].Touch_Card(Cards)    #P1摸牌
            Put_Place_Area(Place_Area, Game, card, who)
        else:
            print("%s的当前手牌："%P[who].name,end=' ')
            for i in P[who].card:
                print(i,end=' ')
            print("\nA:打出手牌\nB:摸牌")
            Operation = str(input('\n请输入要执行的操作:'))
            if Operation == 'B':
                card = P[who].Touch_Card(Cards)  # who摸牌
                Put_Place_Area(Place_Area,Game,card,who)
            elif Operation == 'A':
                card = P[who].Knockout()         #P[who]打出
                Put_Place_Area(Place_Area,Game,card,who)
            elif Operation == 'S':
                break


    else:    # 轮到ai
        tot = 0
        ans = {}
        ans_tot = {}
        ans_choice = ['C', 'D', 'H', 'S', 5]
        for i in ans_choice:
            ans_tot[i] = int(0)
            ans[i] = int(0)
        now = datetime.datetime.now()
        ti = now.hour * 3600 + now.minute * 60 + now.second
        ti_now = now.hour * 3600 + now.minute * 60 + now.second
        dechoice = ['C', 'D', 'H', 'S', 5]    # 1:C, 2:D, 3:H 4:S, 5:摸牌
        dechoice = judge(P[1], dechoice)   # 对P1UCB进行初始化
        while ti < ti_now + 5:
            _vir_card = Card_zu()
            _vir_card.sum = Cards.sum
            for j in Cards.card:
                _vir_card.card.append(j) # 将现在卡组的情况赋值给vir_card，得到卡组区卡牌信息
            r.shuffle(_vir_card.card)    # 在5s内对牌面进行乱序
            # 现在牌面确定
            # print("_gamer: = ", _gamer[1].card)
            tot += 1
            choice = ['C', 'D', 'H', 'S', 5]    # 1:C, 2:D, 3:H 4:S, 5:摸牌
            choice = judge(P[1], choice)   # 对P1UCB进行初始化
            #print(choice)
            UCB = {}                    # 初始化UCB
            for j in choice:
                UCB[j] = [0, 0]
            operation = -1
            ai_times = 100
            for i in range(1, ai_times + 1):    # 对每个确定的牌面模拟1000次对局
                vir_card = Card_zu()
                vir_card.sum = _vir_card.sum
                for j in _vir_card.card:
                    vir_card.card.append(j)
                vir_area = Placement_Area()
                vir_area.sum = Place_Area.sum
                for j in Place_Area.card:
                    vir_area.card.append(j)

                gamer = []
                gamer.append(Player("xxx"))
                gamer.append(Player("hhh"))
                gamer[0].sum = P[0].sum
                for j in P[0].card:
                    gamer[0].card.append(j)
                gamer[1].sum = P[1].sum
                for j in P[1].card:
                    gamer[1].card.append(j)
                # gamer = copy.deepcopy(_gamer)
                _sum = 0
                _ucb = {}
                for j in choice:
                    if UCB[j][1] == 0:
                        _ucb[j] = 1e8
                    else:
                        _ucb[j] = UCB[j][0] * 1.0 / UCB[j][1] + 2.0 * math.sqrt(math.log(i) / UCB[j][1])
                    if _ucb[j] <= 0:
                        _ucb[j] = 1e-2
                    _sum = _sum + _ucb[j]
                _result = random.uniform(0, _sum)
                op = 0
                __sum = 0
                for j in choice:
                    if _ucb[j] == 0:
                        continue
                    if _result >= __sum:
                        op = j
                    __sum = __sum + _ucb[j]
                #op = get_max(UCB, choice, i)     # 得到最大UCB值,然后确定第一步模拟什么
                operation = op
                if op == 5:                     # 如果是5,则直接摸牌
                    v_card = gamer[1].Touch_Card(vir_card)
                    Put_vir_area(vir_area, Game, v_card, 1, gamer)
                else:                         # op为其他情况需要出牌
                    every_card = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
                    for i in every_card:
                        t = str(op) + i
                        if gamer[1].card.count(t) != 0:            # 出牌
                            index = gamer[1].card.index(t)
                            gamer[1].card.pop(index)
                            gamer[1].sum -= 1
                            Put_vir_area(vir_area, Game, v_card, 1, gamer)
                            break

                # 接下来进行双方对战模拟：
                turn = 0
                while vir_card.sum != 0:
                    Choice = ['C', 'D', 'H', 'S', 5]          # 两个玩家的choice
                    Choice = judge(gamer[turn], Choice)
                    op = random.choice(Choice)
                    if op == 5:                             # 需要摸牌
                        v_card = gamer[turn].Touch_Card(vir_card)             # 摸牌
                        Put_vir_area(vir_area, Game, v_card, turn, gamer)

                    else:                                                                # 需要打牌
                        every_card = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
                        for i in every_card:
                            t = str(op) + i
                            if gamer[turn].card.count(t) != 0:  # 出牌
                                index = gamer[turn].card.index(t)
                                gamer[turn].card.pop(index)
                                gamer[turn].sum -= 1
                                Put_vir_area(vir_area, Game, t, turn, gamer)
                                break

                UCB[operation][0] = gamer[1].sum - gamer[0].sum   # Q值
                UCB[operation][1] += 1       # n值
            # 1000次模拟已经结束
            for i in choice:
                if UCB[i][1] != 0:
                    ans[i] = ans[i] + UCB[i][0] * 1.0 / UCB[i][1] + 2.0 * math.sqrt(math.log(ai_times) / UCB[i][1])
                    ans_tot[i] = ans_tot[i] + 1
            now = datetime.datetime.now()
            ti = now.hour * 3600 + now.minute * 60 + now.second
        ans_max = -1e9
        op = 5
        for i in ans_choice:
            if ans_tot[i] != 0:
                # print("i=", i)
                print(ans_tot[i])
                if ans[i] * 1.0 / ans_tot[i] > ans_max:
                    ans_max = ans[i] * 1.0 / ans_tot[i]
                    op = i
        # print("ai op = ", op)
        if op == 5:
            card = P[who].Touch_Card(Cards)  # P1摸牌
            Put_Place_Area(Place_Area, Game, card, who)
        else:
            every_card = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            for i in every_card:
                t = str(op) + i
                if P[who].card.count(t) != 0:  # 出牌
                    index = P[who].card.index(t)
                    P[who].card.pop(index)
                    P[who].sum -= 1
                    # print("出牌:", t)
                    Put_Place_Area(Place_Area, Game, t, who)
                    break
    print("this is who:", who)
    print("卡组：%d" % Cards.sum)
    print(Cards.card)
    print("放堆：%d" % Place_Area.sum)
    print(Place_Area.card)
    print("1P:%d" % P[0].sum)
    print(P[0].card)
    print("2P：%d" % P[1].sum)
    print(P[1].card)
    who = (who + 1) % 2



