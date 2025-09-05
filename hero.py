import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        #TODO Set the hero's name.
        self.health = 1000
        #TODO Set the hero's health. You might give the hero more health than a goblin
        self.power = random.randint(20,50)
        if self.power == 37:
            self.health += 200
        
    
        

        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        damage = self.power
        return damage
        
    def receive_damage(self, damage):
        self.health -= damage
            
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
    
    #TODO define is_alive
    def is_alive(self):
        if self.health > 0:
            return self.health
