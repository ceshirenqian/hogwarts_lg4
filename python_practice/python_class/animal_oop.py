# @time:2020/12/9 18:47
# @author: tq

class Animal:
    def eat(self, calorie):
        print(f"一日三餐不可少, 每天卡路里在{calorie}卡以内")

    def run(self, km):
        print(f"锻炼身体没烦恼，每天坚持跑步{km}公里")

    def sleep(self, hour):
        print(f"每天睡到自然醒, 每天至少要睡{hour}小时")

    def play(self):
        print("小乖乖玩扔球游戏，玩的可开心啦！")

    def roar(self):
        print("老虎不发威，难道是病猫吗！！！")

# 猫
cat = Animal()
cat.eat(100)
# 狗
dog = Animal()
dog.run(5)
# 泰迪
poodle = Animal()
poodle.play()
# 猪
pig = Animal()
pig.sleep(10)
# 老虎
tiger = Animal()
tiger.roar()