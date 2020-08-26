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
    jzi = person(23,9)
    dya = person(23,14)
    # 起始特殊技能
    # 姬子 无
    # 渡鸦
    tmp = random.randint(1,100)
    # print(tmp)
    if tmp <=25:
        dya.act = 1.25 * dya.act

    round = 0
    while True :
        round += 1
        #渡鸦 先攻击
        # 特殊技能
        if round % 3 == 0 :
            jzi.hp = jzi.hp - 7 *(16-jzi.det)
        # 攻击
        else:
            jzi.attacked(dya)
        if jzi.hp <=0 :
            # print("渡鸦胜")
            return 0

        #姬子 后攻击
        # 特殊技能
        if round % 2 == 0:
            jzi.act = jzi.act *2
            jzi.hit = jzi.hit-35
        # 攻击
        if random.randint(1,100) <= jzi.hit:
            dya.attacked(jzi)
        if dya.hp <= 0 :
            # print("姬子胜")
            return 1



if __name__ == "__main__" :
    a = 0
    num = 10000
    for i in range(num) :
        a += run()

    print(a/num)

