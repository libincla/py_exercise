import  random
from time import sleep

class Animal(object):

    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood

    def get_blood(self):
        return self.blood

    def drop_blood(self, blood):

        try:
            blood = int(blood)

        except Exception as e:
            blood = 0

        if self.blood < blood :
            self.blood = 0
        else:
            self.blood = self.blood - blood


    def attack(self, rival):
        num = random.randint(1, 20)
        if isinstance(rival, Animal):
            # if rival.blood > num:
            #     # num = rival.blood
            rival.drop_blood(num)
            print(' %s 对 %s 造成伤害为 %d' % (self.name, rival.name, num))

            # else:
            #     num = rival.blood
            #     rival.drop_blood(num)



        # if isinstance(rival, Animal):
        #     rival.drop_blood(num)
        #
        #     if rival.blood <= num:
        #         num = rival.blood


class Dog(Animal):

    pass

class Cat(Animal):
    pass


wangwang = Dog('wangwang')
miaomiao = Cat('miaomiao', blood=120)

AttackList = [wangwang, miaomiao]

print(wangwang.get_blood(), miaomiao.get_blood())

ROUND = 0
while True:

    if wangwang.get_blood() > 0 and miaomiao.get_blood() > 0:
        wangwang.attack(miaomiao)
        print('miaomiao 的血量是 %d' % miaomiao.get_blood())
        print('=' * 25)
        sleep(2)
        miaomiao.attack(wangwang)
        print('wangwang 的血量是 %d' % wangwang.get_blood())
        print('=' * 25)
        sleep(1)
        ROUND = ROUND + 1
        print('%d round finished' % ROUND)
        print('*' * 30)
    else:
        print('当前wangwang的血是 %d' % wangwang.get_blood())
        print('当前miaomiao的血是 %d' % miaomiao.get_blood())
        if wangwang.get_blood() > miaomiao.get_blood():
            print('wangwang 获胜')
        else:
            print('miaomiao 获胜')
        sleep(1)
        break




