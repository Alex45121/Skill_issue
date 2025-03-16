class GameCharacter():
        def __init__(self,name,health):
                self.name = name
                self._health = health
        
        @property
        def health(self):
                return self._health
        
        @health.setter
        def health(self,value):
                if 0 <= value <= 100:
                        self._health = value
        
        @property
        def is_alive(self):
                if self.health > 0:
                        return True
                else:
                        return False
        @property
        def armor(self):
                if self.health > 80:
                        return True
                else:
                        return False
                

        @health.deleter
        def health(self):
                self._health = 0
                print(f"{self.name} has perished!")
        def __repr__(self):
                return f"{self.name} has {self.health} HP"
        


        
class Hero(GameCharacter):
        def __init__(self,name,health,special_attack):
                super().__init__(name,health)
                self.special_attack = special_attack

        def attack(self,enemy):
                if self.is_alive:
                        damage = 20
                        enemy.health -= damage
                        print(f"{self.name} has dealth {damage} damage to {enemy.name}!")
                else:
                        print(f"{self.name} is dead and cannot attack!")

        def __repr__(self):
                text = super().__repr__()
                return text + f"{self.name} has attacked!"
        



class Enemy(GameCharacter):
        def __init__(self,name,health,damage):
                super().__init__(name,health)
                self.damage = damage
        
        def attack(self,hero):
                if self.is_alive:
                        if hero.armor and self.damage > 0:
                                self.damage / 2
                                hero.health -= self.damage
                                print(f"{self.name} attacks {hero.name} and deals {self.damage} damage!")
                                
                        else:                        
                                hero.health -= self.damage
                                print(f"{self.name} attacks {hero.name} and deals {self.damage} damage!")
                else:
                        print(f"{self.name} is dead and cannot attack.")
        def __repr__(self):
                text = super().__repr__()
                return text + f"{self.name} has attacked!"
                
