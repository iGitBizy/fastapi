## OBJECT ORIENTED PROGRAMMING
 - scalability
 - efficiency
 - reusability

 ### 2 ways to define an object
- behaviors (what an object does)
    - bark, eat, sleep, run
- states (what an object is)
    - 4 legs, 2 ears, goldendoodle, etc 

### 4 Pillars of OOP
- Encapsulation
    - refers to the Bundling of data
    - change public attributes to be private so they cannot be changes
- Abstraction
    - interface that allows a user to turn on/off functionality without needing to understand
    - hide implementation and only show necessary details
- Inheritance
    - Inheritance is the process of acquiring properties from one class to the next
    - creates hierachy between classes
- Polymorphism
    - means to have many forms
    - changing an object at a specific runtime

### Create a game where enemies fight each other
#### Criteria
- Enenmies that can fight each other
- different type of enemies
    - zombie
    - ogre
- each enemy has diff powers, health points and attack damage

#### implement using 4 pillars of oop

- create enemy object
    - name/ type 
    - health points
    - attack damage

#### Time to battle
- give enemies special attacks
- Add code to the Enemy(Parent) Both Zombie and Ogre

#### What is composition
- way to create objects made up of other objects
- class contains one or more objects of another class as instance variables
- provide layered functionality to the object
- known as a HAS-A relationship ex. vehicle -- has an engine