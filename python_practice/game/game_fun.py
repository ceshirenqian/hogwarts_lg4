# @time:2020/12/9 15:26
# @author: tq

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
不知道敌人的血量，希望是随机的数字
两个hp进行对比，血量剩余多的人获胜
"""
import random


def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    # 打印敌人的血量和攻击力
    print(f"敌人血量：{enemy_hp},敌人的攻击力：{enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断谁的血量小于等于0
        if my_hp <= 0:
            print(f"我的血量：{my_hp},敌人的血量：{enemy_hp}")
            print("我输了")
            # 满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print(f"我的血量：{my_hp},敌人的血量：{enemy_hp}")
            print("你赢了")
            break

#main函数入口
if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    # 让敌人的血量从hp列表随机挑选一个值
    enemy_hp = random.choice(hp)

    # 敌人的攻击力用randint方法生成随机整数
    enemy_power = random.randint(100,300)

    # 调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)
