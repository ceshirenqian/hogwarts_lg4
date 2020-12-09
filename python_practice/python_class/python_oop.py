# @time:2020/12/9 16:59
# @author: tq

# 类名起名要符合语法和规范，类名命名规则：驼峰
# 面向对象
class House:
    # 静态属性-》类变量（类之中，方法之外）
    door = "red"
    floor = "white"

    # 构造函数，类实例化的时候直接执行
    def __init__(self):
        # 在方法当中调用变量需要加上self
        print(self.door)
        # 实例变量, 类当中，方法当中，以"self.变量名"方式定义
        self.kitchen ="cook"

    # 动态方法
    def sleep(self):
        # 普通变量：类当中，方法当中
        bed ="席梦思"
        self.table = "桌子上可以放好吃的东西"
        print(f"在房子里可以躺在{bed}上睡觉")

    def cook(self):
        print(self.table)
        print(f"在房子里可以在{self.kitchen}做饭")

#把类实例化,才能使用
#北欧风房子（对象，访问方法和属性）
north_house = House()
#中式风房子
china_house = House()
# 调用类属性
# print(House.door)
# 修改类属性
# House.door = "grey"
# print(House.door)
# # 实例对象调用类属性
# print(north_house.door)
# 修改对象的属性
# north_house.door = "black"
# print(north_house.door)
# print(House.door)
# print(china_house.door)

china_house.sleep()
china_house.cook()

