class Animal(object):
    
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1;    
        return self

    def run(self):
        self.health -= 5
        return self
        
    def display_health(self):
        print(str(self.health))
        return self

class Dog(Animal):
    
    def __init__(self, name):
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5;    
        return self
    
class Dragon(Animal):
    
    def __init__(self, name):
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
        
    def display_health(self):
        super(Dragon, self).display_health()
        print("I am a dragon")
        return self

newAnimal = Animal("Animal", 100)
newAnimal.walk()
newAnimal.walk()
newAnimal.walk()
newAnimal.run()
newAnimal.run()
newAnimal.display_health()

newDog = Dog("Dog")
newDog.walk()
newDog.walk()
newDog.walk()
newDog.run()
newDog.run()
newDog.pet()
newDog.display_health()

drag = Dragon("Dragon")
drag.walk()
drag.walk()
drag.run()
drag.run()
drag.fly()
drag.display_health()

#a = Animal("A", 100)
#a.pet()
#a.fly()
#a.display_health()