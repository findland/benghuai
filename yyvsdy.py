import random
class person:
    def __init__(self,act,det,hp=100,hit=100):
        self.act = act
        self.det = det
        self.hp = hp
        self.hit = hit
    def attacked(self,person):
        self.hp = self.hp - (person.act - self.det)
    def __str__(self):
        n = ""
        n += "攻击力：" + str(self.act) + "\n"
        n += "防御力：" + str(self.det) + "\n"
        n += "速度：" + str(self.sep) + "\n"
        n += "Hp: " + str(self.hp) + "\n"
        return n

    __repr__ = __str__


def run():
    dya = person(23,14) # 渡鸦
    yay = person(22,12) # 芽衣
    # 起始特殊技能
    # 渡鸦
    if random.randint(1, 100) <= 25:
        dya.act = 1.25 * dya.act
    # 芽衣 无
    round = 0
    while True :
        round += 1
        #芽衣 先攻击
        # 特殊技能
        if round % 2 == 0 :
            dya.hp = dya.hp - 5 * 3
        # 攻击
        else:
            dya.attacked(yay)
        # 芽衣特殊技能30%麻痹
        if dya.hp <=0 :
            # print("芽衣胜")
            return 1
        if random.randint(1, 100)<=30:
            continue

        # 渡鸦 后攻击
        # 特殊技能
        if round % 3 == 0:
            yay.hp = yay.hp - 7 * (16 - yay.det)
        # 攻击
        else:
            yay.attacked(dya)
        if yay.hp <= 0:
            # print("渡鸦胜")
            return 0

if __name__ == "__main__" :
    a = 0
    num = 100000
    for i in range(num) :
        a += run()

    print(a/num)