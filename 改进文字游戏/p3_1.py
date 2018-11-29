import random

secret = random.randint(1,10)
temp = input("不妨猜一下闫善浩心里想的是哪个数字：")
guess = int(temp)


while guess != secret:
    temp = input("哎呀，猜错了，重新输入吧：")
    guess = int(temp)

    if guess == secret:
        print("哎呀，你是闫善浩肚子里的蛔虫吗？")
        print("哼~猜中了也没奖励")

    else:
        if guess > secret:
            print("哥，大了")
        else:
            print("哥，小了")
print("游戏结束，不玩了")
