import random
class plaer():
    def __init__(self,php,patac,levl,oz):
        self.php = php
        self.patac = patac
        self.levl = levl
        self.plaeroz = oz

class enemy():
    def __init__(self,ehp,eatac):
        self.ehp = ehp
        self.eatac = eatac

php = 100
patac = random.randint(10,25)
levl = 1
plaeroz = 0
ehp = random.randint(60,90)
eatac = random.randint(10,20)

plae = plaer(php,patac,levl,plaeroz)
enem = enemy(ehp,eatac)

def fight(plae,enem):
    print('******************************')
    print('ваше здоровье',plae.php,'едениц.')
    print('здоровье противника', enem.ehp, 'едениц.')
    ehp = enem.ehp

    if plae.php > 0:
        while ehp > 0:
            print('ваши действия?')
            n = int(input('1)атаковать 2)востановить здоровье: '))
            if n == 1:
                ehp = ehp - plae.patac
                if ehp < 0:
                    ehp = 0
                print('вы атаковали противника, у него осталось',ehp,'здоровья.')
                plae.php = plae.php - enem.eatac
                if plae.php > 100:
                    plae.php = 100
                if plae.php < 0:
                    plae.php = 0
                print('противник ударил вас, у вас осталось',plae.php,'здоровья.')
            elif n == 2:
                os = random.randint(10,20)
                plae.php = plae.php + os
                print('вы востановили здаповье на',os,'едениц, теперь у вас',plae.php,'едениц здаровья.')
            else: print('*ошибка ввода*')
        print('******************************')
        print('противник повержен')
        os = random.randint(25,50)
        plae.php = plae.php + os
        if plae.php > 100:
            plae.php = 100
        oz = random.randint(25,50)
        plae.plaeroz = plae.plaeroz + oz
        print('вы получили',oz,'едениц опыта и востановили свое здаровье.')
        print('ваш текущий уровень',plae.levl,', ваше количество здоровья',plae.php,'едениц.')
    else: print('вы проиграли.')



for i in range(5):
    fight(plae,enem)
    print(plae.plaeroz)