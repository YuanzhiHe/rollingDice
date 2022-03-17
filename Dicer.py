# Author: Martin He
# School of Computer Science, University of Birmingham
# 2022-3-14

import random

diceList = []
AIdice = []
kai = False
callone = False


# 摇骰子，顺子重摇
def rolling():
    print("-----------开始-----------")
    global diceList
    global AIdice
    setlist1 = {}.fromkeys(diceList)
    setlist2 = {}.fromkeys(AIdice)
    while len(setlist1) == len(diceList) or len(setlist2) == len(AIdice) or len(diceList) == 0:
        diceList = []
        AIdice = []
        for i in range(5):
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)
            diceList.append(dice1)
            AIdice.append(dice2)
        setlist1 = {}.fromkeys(diceList)
        setlist2 = {}.fromkeys(AIdice)
    list.sort(diceList)
    list.sort(AIdice)
    print("你本次的骰子是%s" % diceList)


def start_game():
    global kai, inputnum, callone
    first = 3
    second = 0
    # 开始喊，最多10轮
    for i in range(10):
        calling = False
        # 检测输入是否正常
        while not calling:
            inputnum = input("请喊：")
            if inputnum == '开':
                kai = True
                calling = True
            elif len(inputnum) != 2:
                print('会玩吗？')
            elif inputnum == '21':
                calling = True
            elif int(inputnum[0]) < first:
                print('会玩吗？')
            elif int(inputnum[1]) == 1:
                if second == 1 and int(inputnum[0]) == first:
                    print('会玩吗？')
                else:
                    calling = True
            else:
                if int(inputnum[1]) < 1 or int(inputnum[1]) > 6:
                    print('会玩吗？')
                elif int(inputnum[0]) == first and int(inputnum[1]) <= second:
                    print('会玩吗？')
                else:
                    calling = True
        if inputnum == '开':
            break
        first = int(inputnum[0])
        second = int(inputnum[1])
        if second == 1:
            callone = True

        rand = random.random()  # 随机性
        # 当骰子是豹子时，只喊自己的数
        if AIdice.count(AIdice[4]) + AIdice.count(1) == 5:
            if second == AIdice[4]:
                print('加一个,%d个%d' % (first + 1, second))
                first = first + 1
            elif second < AIdice[4]:
                print('%d个%d' % (first, second))
                first = first + 1
            else:
                print('%d个%d' % (first + 1, second))
                first = first + 1
        # 当喊的骰子数已经不可能存在时，直接开
        elif AIdice.count(second) + AIdice.count(1) + 7 < first:
            break
        elif (AIdice.count(second) + AIdice.count(1) - first < 0) and not callone:
            # 当电脑没有足够的骰子时有0.2的概率直接开
            if rand > 0.8:
                break
            elif 0.8 > rand > 0.3:
                temp = second
                tempcount = (0, 0)
                run = False
                while temp <= 6:
                    temp = temp + 1
                    if AIdice.count(temp) + AIdice.count(1) > tempcount[1]:
                        tempcount = (temp, AIdice.count(temp) + AIdice.count(1))
                temp = 2
                while temp <= second:
                    if AIdice.count(temp) > tempcount[1]:
                        tempcount = (temp, AIdice.count(temp) + AIdice.count(1))
                    temp = temp + 1
                # 当喊到4个以上的骰子数时，有40%概率加一或喊其它自己有的骰子，10%概率吹牛
                if first >= 4:
                    if tempcount[1] >= AIdice.count(second) + AIdice.count(1) and 0.3 < rand < 0.7:
                        if tempcount[0] < second:
                            second = tempcount[0]
                            print('%d个%d' % (first + 1, second))
                            first = first + 1
                        elif tempcount[0] == second:
                            print('加一个,%d个%d' % (first + 1, second))
                            first = first + 1
                        else:
                            second = tempcount[0]
                            print('%d个%d' % (first, second))
                    else:
                        run = True
                # 4个以下骰子数时，有30%概率加一或喊其它自己有的骰子，20%概率吹牛
                else:
                    if tempcount[1] >= AIdice.count(second) + AIdice.count(1) and 0.4 < rand < 0.7:
                        if tempcount[0] < second:
                            second = tempcount[0]
                            print('%d个%d' % (first + 1, second))
                            first = first + 1
                        elif tempcount[0] == second:
                            print('加一个,%d个%d' % (first + 1, second))
                            first = first + 1
                        else:
                            second = tempcount[0]
                            print('%d个%d' % (first, second))
                    else:
                        run = True
                # 吹牛
                if run:
                    newdice = second
                    while newdice == second:
                        newdice = random.randrange(2, 7)
                    if newdice < second:
                        second = newdice
                        print('%d个%d' % (first + 1, second))
                        first = first + 1
                    else:
                        second = newdice
                        print('%d个%d' % (first, second))
            # 剩下0.2的概率
            else:
                # 没喊过1，如果自己手里的当前数的数量比喊的数量少至多一个以下，加一个
                if second != 1 and AIdice.count(second) + AIdice.count(1) - first >= -1:
                    print('加一个,%d个%d' % (first + 1, second))
                    first = first + 1
                else:
                    break
        else:
            # 喊过1了。
            # 如果当前喊的是1，只要手里1的数量不够，40%概率开，60%概率喊其它数
            # 如果当前喊的不是1，如果自己手里的当前数的数量比喊的数量少至多一个以下，加一个
            if second != 1 and AIdice.count(second) - first >= -1:
                print('加一个,%d个%d' % (first + 1, second))
                first = first + 1
            elif second == 1 and AIdice.count(1) - first >= 0:
                print('加一个,%d个%d' % (first + 1, second))
                first = first + 1
            elif 0.8 > rand > 0.2:
                temp = second
                tempcount = (0, 0)
                first = first + 1
                while temp <= 6:
                    temp = temp + 1
                    if AIdice.count(temp) > tempcount[1]:
                        tempcount = (temp, AIdice.count(temp))
                temp = 2
                while temp <= second:
                    if AIdice.count(temp) > tempcount[1]:
                        tempcount = (temp, AIdice.count(temp))
                    temp = temp + 1
                if first >= 3:
                    if tempcount[1] >= AIdice.count(second):
                        second = tempcount[0]
                        print('%d个%d' % (first, second))
                else:
                    if tempcount[1] >= AIdice.count(second) and 0.2 < rand < 0.7:
                        if tempcount[0] < second:
                            second = tempcount[0]
                            print('%d个%d' % (first + 1, second))
                            first = first + 1
                        elif tempcount[0] == second:
                            print('加一个,%d个%d' % (first + 1, second))
                            first = first + 1
                        else:
                            second = tempcount[0]
                            print('%d个%d' % (first, second))
                    else:
                        newdice = second
                        while newdice == second:
                            newdice = random.randrange(2, 7)
                        if newdice < second:
                            second = newdice
                            print('%d个%d' % (first + 1, second))
                            first = first + 1
                        elif tempcount[0] == second:
                            print('加一个,%d个%d' % (first + 1, second))
                            first = first + 1
                        else:
                            second = newdice
                            print('%d个%d' % (first, second))
            else:
                break

    # 开
    if not kai:
        print("-----我不信你，你被开了-----")
    else:
        print("-----开-----")
    print("我的骰子是：%s" % AIdice)

    # 开始计算结果
    if not callone:
        # 没喊过1,1仍然可以作为任何数
        ai = AIdice.count(second) + AIdice.count(1)
        player = diceList.count(second) + diceList.count(1)
    elif first == 1:
        # 当前喊的数字是1
        ai = AIdice.count(1)
        player = diceList.count(1)
    else:
        # 喊过1了，1不再作为任何数
        ai = AIdice.count(second)
        player = diceList.count(second)

    # 豹子算6个，金钱豹算7个
    if AIdice.count(second) == 5:
        ai = ai + 2
    elif ai == 5:
        ai = ai + 1
    if diceList.count(second) == 5:
        player = player + 2
    elif player == 5:
        player = player + 1

    if not kai:
        if ai + player < first:
            print('你输了')
        else:
            print('你赢了')
    else:
        if ai + player < first:
            print('你赢了')
        else:
            print('你输了')


rolling()
start_game()
