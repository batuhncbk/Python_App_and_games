import random as rdm

class Person():

    def __init__(self,hp,ap,gold):
        self.hp = hp
        self.ap = ap
        self.gold = gold

    def attack(self,ap):
        damage = rdm.randint(0,self.ap)
        return damage

hero = Person(100,15,0)
monster = Person(40,5,0)

