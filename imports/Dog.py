# create animal class
class Animal:
    weight: int
    color: str
    age: int
    animal_type: str

    def eat(self):
        print("Animal eating")

    def sleep(self):
        print('Animal sleeping')

# dog as an object
# class Dog:
#     legs: int = 4
#     ears: int = 2
#     type: str = 'Goldendoodle'
#     age:  int = 5
#     color: str = 'Yellow'

# create dog class with animal properties
class Dog(Animal):
    """ All Animal Attributes"""
    can_shed: bool
    domestic_name: str

    def talk(self):
        print('Bark')

    def eat(self):
        print('Chews on bone!') # method overiding parent class

    """ All Animal Methods"""

class Bird(Animal):
    """ All Animal Attributes"""
    birdType: str

    def talk(self):
        print('Chirp')

    def fly(self):
        print('Begins to soar')

    """ All Animal Methods"""

##### super vs self in python objects
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Student(Person):
    def __init__(self, name, age, degree):
         # Student users 'super' to call on parent constructor
         # which assigns properties name and age
        super().__init__(name=name, age=age)
        # student uses 'self' to reference degree which is diff from degree
        # parameter/argument coming in 
        self.degree = degree