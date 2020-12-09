# @time:2020/12/9 15:16
# @author: tq

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 定义一个fight方法
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(f"我的血量：{my_hp},敌人的血量：{enemy_hp}")
        # 判断谁的血量小于等于0
        if my_hp <= 0:
            print("我输了")
            #满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break

#调用fight方法
fight()