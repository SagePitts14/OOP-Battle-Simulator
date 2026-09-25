import random

class Wizard:

     def int_(self, name):
        self.name=name
        self.health=200
        if random.randint(1,5) < 5:
            self.attack_power=random(1,4)*10
        else:
            self.attack_power=100
          

def attack(self):   
        """Return a random amount of damage."""
        return random.randint(0, self.attack_power) 
def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.health == 0 
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0

pass