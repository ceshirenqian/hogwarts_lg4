# @time:2020/12/9 18:29
# @author: tq

from python_practice.python_class.tonglao import TongLao

# 继承父类
class XuZhu(TongLao):

    def __init__(self, hp, power):
        # 通过继承调用父类的构造函数，拿到父类的属性
        super().__init__(hp, power)
        print(hp)
        print(power)

    def read(self):
        print("罪过罪过")

if __name__ == "__main__":
    xuzhu = XuZhu(60, 30)
    xuzhu.ee_people("丁春秋")
    xuzhu.read()
    print(f"防御值为：{xuzhu.defense}")
