# @time:2020/12/9 16:58
# @author: tq
from python_practice.python_class.tonglao import TongLao
from python_practice.python_class.xuzhu import XuZhu

if __name__ == "__main__":
    # 实例化童姥类
    tonglao = TongLao(200, 50)
    tonglao.ee_people("L SQ")
    tonglao.fight_zms(300, 20)

    # 实例化虚竹类
    xuzhu = XuZhu(10, 70)
    xuzhu.read()
