from abc import ABC, abstractmethod

class Creature:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health
        self.max_health = health

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures


    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        self.hit(c1,c2)
        self.hit(c2,c1)

        alive1 = c1.health > 0
        alive2 = c2.health > 0

        if alive1 and alive2:
            return -1
        if alive1:
            return c1_index
        if alive2:
            return c2_index
        else:
            return -1

    @abstractmethod
    def hit(self, attacker, defender):
        pass

    
class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.damage
        alive = defender.health > 0
        if alive:
            defender.health = defender.max_health
            return True
        else:
            return False

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.damage
        return defender.health > 0


creatures = [Creature(1, 2), Creature(1, 3)]
game = PermanentDamageCardGame(creatures)
print(game.combat(0, 1))
print(game.combat(0, 1))
