# create child class of Enemy
from enemy import *
import random

class Zombie(Enemy): 
    # define parameter constructor
    def __init__(self, health_points, attack_damage):
        # call super class to inherent enemy properties for health and attack
        super().__init__(type_of_enemy= 'Zombie',
                         health_points= health_points,
                         attack_damage= attack_damage)
    
    # method overwriting   
    def talk(self):
        print('*Grumbling...*') 
    # new zombie only meth
    def spread_disease(self):
        print('The Zombie is trying to spread infection.') 
    
    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 20
            print('Zombie regenerated 20 HP!')