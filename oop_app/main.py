# import enemy class
from enemy import *
from zombie import *
from ogre import *

# # create new enemy object
# zombie = Enemy('Zombie', 10, 1) # calling Enemy constructor with paramaters
# big_zombie = Enemy('Big Zombie', 50, 10)

# zombie.get_type_of_enemy()

# zombie.talk()
# zombie.stats()
# zombie.walk_forward()
# zombie.attack()

zombie = Zombie(10, 3)
ogre = Ogre(9, 4)

print(zombie.get_type_of_enemy())
zombie.stats()
zombie.talk()
zombie.walk_forward()
print('\n')

print(ogre.get_type_of_enemy())
ogre.stats()
ogre.talk()
ogre.walk_forward()