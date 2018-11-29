bingo = '小甲鱼很帅'
l_pj = ('滚','混蛋','yazi','gundan','gungun')
while True:
    a = input("请输入你形容小甲鱼的一句话：")
    if a in l_pj:
        print('我很不高兴，我愤怒了')
        break
    elif a == bingo:
            print('哎呦不错哦')
            break
    else:
        print('抱歉，错了，请重新输入（回答正确才能退出游戏）')

print('~~~~~~~~游戏结束~~~~~~~~~')
