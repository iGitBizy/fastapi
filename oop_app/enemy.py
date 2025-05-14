# define enemy object states
# class Enemy:
#     # # class attributes
#     # type_of_enemy: str
#     # health_points: int = 10
#     # attack_damage: int = 1

#     # # default or empty constructor example
#     # def __init__(self): #auto created if no constructor is found
#     #     pass

#     # # no argument constructor example
#     # def __init__(self):
#     #     print("New enemy created with no starting values")

#     # # parameter constructor example
#     # def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
#     #     #  these are public variables which means someone can change them
#     #     self.type_of_enemy = type_of_enemy
#     #     self.health_points = health_points
#     #     self.attack_damage = attack_damage
#     #     # uasage: enemey = Enemy('Zombie', 15, 3)

#     # parameter constructor example 
#     # implement encapsulation
#     def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
#         #  these are public variables which means someone can change them
#         self.__type_of_enemy = type_of_enemy # use dbl __ so you cannot change
#         self.health_points = health_points
#         self.attack_damage = attack_damage

#     # if you absolutely have to change the type_of_enemy use getter and setter
#     # funnctions akak implement encapsulation
#     # return type of enemy
#     def get_type_of_enemy(self):
#         return self.__type_of_enemy 
#     # set type of enemey
#     # def set_type_of_enemy(self, type_of_enemy):
#     #     self__type_of_enemy = type_of_enemy 
    

#     def stats(self):
#         print(f'{self.__type_of_enemy} has {self.health_points} health points And can do attack of {self.attack_damage} \n')

#     def talk(self):
#         print(f'I am a {self.__type_of_enemy}. Be prepared to fight!')

#     def walk_forward(self):
#         print(f'{self.__type_of_enemy} moves closer to you.')

#     def attack(self):
#         print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')


# Implement inheritance use enemy as parent class
# create two children classes zombie and ogre
class Enemy: # parent class
    # create parameter constructor
    def __init__(self, type_of_enemy, health_points, attack_damage):
        # define attributes
        self.__type_of_enemy = type_of_enemy # private variable
        self.health_points = health_points
        self.attack_damage = attack_damage

    # define methods 
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

# class Zombie(Enemy): # child class of Enemy
#     # define parameter constructor
#     def __init__(self, health_points, attack_damage):
#         # call super class to inherent enemy properties for health and attack
#         super().__init__(type_of_enemy='Zombie',
#                          health_points= health_points,
#                          attack_damage= attack_damage)
    
#     # method overwriting   
#     def talk(self):
#         print('*Grumbling...*') 
#     # new zombie only meth
#     def spread_disease(self):
#         print('The Zombie is trying to spread infection') 
    
# class Ogre(Enemy):

#     def __init__(self, health_points, attack_damage):

#         super().__init__(type_of_enemy='Ogre',
#                          health_points= health_points,
#                          attack_damage= attack_damage)
        
#     def talk(self):
#         print('Ogre is slamming hands all around.')

    

    
    