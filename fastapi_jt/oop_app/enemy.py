# define enemy object states
# Implement inheritance use enemy as parent class
# create two children classes zombie and ogre
class Enemy: # parent class
    # create parameter constructor
    def __init__(self, type_of_enemy, health_points, attack_damage):
        # define attributes
        self.__type_of_enemy = type_of_enemy # private variable
        self.health_points = health_points
        self.attack_damage = attack_damage

    # define methods ``
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')

    def stats(self):
        print(f'{self.__type_of_enemy} has {self.health_points} health points And can do attack of {self.attack_damage}')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def special_attack(self):
        print(f'Enemy has no special attack')

    
    