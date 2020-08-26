import random
class person:
    def __init__(self,act,det,hp=100,hit=100):
        self.act = act
        self.det = det
        self.hp = hp
        self.hit = hit
    def attack(self,person):
        person.hp = person.hp - (self.act - person.det)
    def __str__(self):
        n = ""
        n += "攻击力：" + str(self.act) + "\n"
        n += "防御力：" + str(self.det) + "\n"
        n += "Hp: " + str(self.hp) + "\n"
        return n

    __repr__ = __str__


def run():
    yil = person(20,9) # 樱莲
    dls = person(19,12) # 德莉莎

    # 初始特殊技能
    # 无

    round = 0
    while True:
        round += 1
        # 德莉莎 先攻
        if round % 3 ==0:
            yil.hp = yil.hp -5*(16-yil.det)
        else:
            dls.attack(yil)
        # 特殊攻击
        if random.randint(1,100)<=30:
            yil.det -= 5
        if yil.hp <= 0 :
            # print("德莉莎胜")
            return 1

        #樱莲 后攻
        if random.randint(1, 100) <= 30:
            yil.hp += 25
        if round % 2  == 0 :
            dls.hp -=25
        else:
            yil.attack(dls)
        if dls.hp <= 0 :
            # print("樱莲胜")
            return 0



if __name__ == "__main__" :
    # run()
    a = 0
    num = 10000
    for i in range(num) :
        a += run()

    print(a/num)