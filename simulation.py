import random
import datetime
class Person:
    def __init__(self,name,act,det,spe,hp=100,skip=0,sround=0,hit=100,times = 1.0):
        self.act = act
        self.det = det
        self.hp = hp
        self.spe =spe
        self.name = name
        self.skip = skip
        self.sround = sround
        self.hit = hit
        self.times = times

    def revage(self,p1):
        if p1.name=="幽兰黛尔":
            if random.randint(1,100)<=16:
                if random.randint(1, 100) <= p1.hit:
                    self.hp -= 30 - self.det
                return 1
            else:
                return 0


    # def Dmg(self):
    #     pass
    def is_dead(self):
        return self.hp <= 0
    def base_attack(self,person):
        return (self.act - person.det)
    def attack(self,p1,round):
        # print("DMG:",self.Dmg(p1,round),"\nHP:",p1.hp)
        if self.skip == 1:
            self.skip = 0
        else:
            p1.hp -= self.times*self.Dmg(p1,round)
    def __str__(self):
        n = ""
        n += self.name+"\n"
        n += "攻击力：" + str(self.act) + "\n"
        n += "防御力：" + str(self.det) + "\n"
        n += "Hp: " + str(self.hp) + "\n"
        return n

    __repr__ = __str__

class Yil(Person): # 樱莲
    def __init__(self):
        Person.__init__(self,"樱莲",20,9,18)
    def Dmg(self,p1,round):
        dmg = 0
        if random.randint(1,100)<=30:
            self.hp += 25
            if self.hp >100 :
                self.hp = 100
        if round %2 ==0:
            if self.revage(p1):
                return dmg
            if random.randint(1, 100) <= self.hit:
                dmg += 25
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
        return dmg

class Dls(Person): # 德莉莎
    def __init__(self):
        Person.__init__(self,"德莉莎",19,12,22)

    def Dmg(self, p1, round):
        dmg = 0
        if round%3 ==0 :
            if self.revage(p1):
                return dmg
            for i in range(5):
                if random.randint(1, 100) <= self.hit:
                    dmg += (16-p1.det)
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
        if random.randint(1,100)<=30:
            p1.det -=5
        return dmg


class Dya(Person): # 渡鸦
    def __init__(self,P1):
        Person.__init__(self, "渡鸦", 23, 14, 14)
        if P1.name == "琪亚娜":
            self.act = 1.25 * self.act
        else:
            # pass
            if random.randint(1, 100) <= 25:
                self.act = 1.25 * self.act
    def Dmg(self,p1,round):
        dmg = 0
        if round %3 ==0:
            if self.revage(p1):
                return dmg
            for i in range(7):
                if random.randint(1, 100) <= self.hit:
                    dmg += (16-p1.det)
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
        # print("渡鸦：",dmg)
        return dmg



class Jiz(Person): # 姬子
    def __init__(self):
        self.muti = ["阿琳姐妹","德莉莎","樱莲"]
        Person.__init__(self,"姬子",23,9,12)
    def Dmg(self,p1,round):
        dmg = 0
        if round%2 == 0:
            self.act *= 2
            self.hit -= 35
        if random.randint(1, 100) <= self.hit:
            dmg += self.base_attack(p1)
        if p1.name in self.muti:
            dmg = dmg*2
        return dmg




class Yay(Person): # 芽衣
    def __init__(self):
        Person.__init__(self,"芽衣",22,12,30)
    def Dmg(self,p1,round):
        dmg = 0
        if round %2 == 0 :
            if self.revage(p1):
                return dmg
            for i in range(5):
                if random.randint(1, 100) <= self.hit:
                    dmg += 3
        else:
            dmg += self.base_attack(p1)
        if random.randint(1,100)<=30:
            p1.skip = 1
        return dmg



class Ali(Person): # 阿琳姐妹
    def __init__(self):
        Person.__init__(self,"阿琳姐妹",18,10,10)
        self.dead_attack = 1
        self.speal_attack = 1
    def is_dead(self):
        if self.hp<=0:
            if self.dead_attack == 0:
                return True
            else:
                self.dead_attack = 0
                self.hp = 20
                return False
    def Dmg(self,p1,round):
        dmg = 0
        if self.dead_attack == 0 and self.speal_attack == 1:
            self.speal_attack = 0
            if self.revage(p1):
                return dmg
            if random.randint(1,100) <=50:
                if random.randint(1, 100) <= self.hit:
                    dmg += 233-p1.det
            else:
                if random.randint(1, 100) <= self.hit:
                    dmg += 50 -p1.det
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
        return dmg


class Kna(Person):
    def __init__(self):
        Person.__init__(self,"琪亚娜",24,11,23)
    def Dmg(self,p1,round):
        dmg = 0
        if round %2 ==0:
            if self.revage(p1):
                return dmg
            if random.randint(1, 100) <= self.hit:
                dmg += self.act + p1.det
            if random.randint(1,100) <=35:
                self.skip = 1
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
        # print("琪亚娜：",dmg)
        return dmg


class Bly(Person): # 布洛妮娅
    def __init__(self):
        Person.__init__(self,"布洛妮娅",21,10,20)
    def Dmg(self,p1,round):
        dmg = 0
        if round % 3 == 0 :
            if self.revage(p1):
                return dmg
            if random.randint(1, 100) <= self.hit:
                dmg += random.randint(1,100)
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
        if random.randint(1,100) <=25:
            for i in range(4):
                if random.randint(1, 100) <= self.hit:
                    dmg += (12-p1.det)
        return dmg



class Lit(Person):
    def __init__(self):
        Person.__init__(self,"丽塔",26,11,17)
        self.flag =1
    def Dmg(self,p1,round):
        dmg = 0
        if round %4 == 0:
            if self.revage(p1):
                return dmg
            p1.hp +=4
            if p1.hp >100:
                p1.hp = 100
            p1.sround = 2
            if self.flag :
                self.flag = 0
                p1.times = 0.4

        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.base_attack(p1)
            if random.randint(1,100)<=35:
                dmg -= 3
                if dmg < 0 :
                    dmg = 0
                p1.act -= 4
                if p1.act <0:
                    p1.act = 0
        return  dmg


class Xer(Person):
    def __init__(self):
        Person.__init__(self,"希儿",23,13,26)
        self.black_white = 1
    def Dmg(self,p1,round):
        dmg = 0
        if self.black_white:
            self.black_white=0
            self.act +=10
            self.det -=5
        else:
            self.black_white =1
            self.act -=10
            self.det +=5
            self.hp += random.randint(1,15)
            if self.hp  >100 :
                self.hp = 100
        if random.randint(1,100) <= self.hit:
            dmg += self.base_attack(p1)
        return dmg

class Dae(Person): # 幽兰黛尔
    def __init__(self):
        Person.__init__(self,"幽兰黛尔",19,10,15)
    def Dmg(self,p1,round):
        dmg =0
        self.act += 3
        if random.randint(1,100) <= self.hit:
            dmg += self.base_attack(p1)
        return  dmg

class Fuh(Person): #符华
    def __init__(self):
        Person.__init__(self,"符华",17,15,16)
    def Dmg(self,p1,round):
        dmg = 0
        if round %3 ==0:
            if self.revage(p1):
                return dmg
            if random.randint(1, 100) <= self.hit:
                dmg += 18
            p1.hit -= 25
        else:
            if random.randint(1, 100) <= self.hit:
                dmg += self.act
        return dmg



def first():
    P1 = Dls()
    P2 = Dya(P1)
    if P1.spe < P2.spe:
        P1,P2 = P2,P1
    return P1,P2

def fight():
    P1 , P2 = first()
    round = 0
    while True:
        round += 1
        # P1 先攻
        # print (round)
        P1.attack(P2,round)
        if P1.is_dead():
            return 0
        if P2.is_dead():
            return 1

        # P2 后攻
        P2.attack(P1,round)
        if P1.is_dead():
            return 0
        if P2.is_dead():
            return 1

if __name__ == "__main__" :
    # run()
    P1,P2 = first()
    num = 10000
    a= 0
    for i in range(num):
        a += fight()
    print (P1.name , "的胜率是：",a/num)
    print (P2.name , "的胜率是：",1-a/num)
