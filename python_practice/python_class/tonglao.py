# @time:2020/12/9 18:07
# @author: tq

"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
1: ee_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”
2: fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。
每次调用都会打印“罪过罪过”
加入模块化改造
"""

class TongLao:
    # 构造函数,参数hp为我方血量，power为我方攻击力
    def __init__(self, hp, power):
        self.defense = 100
        self.hp = hp
        self.power = power

    # 根据角色识别人物口头禅
    def ee_people(self, name):
        name = name.replace(" ","")
        if (name == "WYZ" or name == "无崖子") :
            print("师弟！！！！")
        elif (name == "LSQ" or name == "李秋水") :
            print("师弟是我的！")
        elif (name == "DCQ" or name == "丁春秋"):
            print("叛徒！我杀了你")
        else:
            print("不好意思，没人认识你")

    # 一回合制对打
    def fight_zms(self, enemy_hp, enemy_power):
        print(f"敌人血量是：{enemy_hp}，敌人攻击力为：{enemy_power}")
        print(f"我的血量是：{self.hp}，我的攻击力为：{self.power}")
        # 提升自己的武力值提10倍，血量缩减2倍
        self.hp = self.hp / 2
        self.power = self.power * 10

        print(f"提升修炼后，我的血量是：{self.hp}，我的攻击力为：{self.power}")
        # 与敌方攻击，计算剩余血量
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power

        if enemy_hp > self.hp :
            print(f"敌方获胜, 敌方血量：{enemy_hp}，我方血量：{self.hp}")
        elif enemy_hp < self.hp :
            print(f"我方获胜, 我方血量：{self.hp}，敌方血量：{enemy_hp}")
        else:
            print("平局")

if __name__ == "__main__":
    tonglao = TongLao(200, 50)
    tonglao.ee_people("L SQ")
    tonglao.fight_zms(300, 20)




