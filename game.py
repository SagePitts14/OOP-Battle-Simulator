from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Rectangle"



def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

goblin = Goblin("D0rian")

hero =  Hero("Trip T")


goblin2 = Goblin("Ashtung")
    
print(f"{goblin.name} enters the arena with {goblin.health} health.")
print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
print(f"But {hero.name} has answered the call")
goblin.take_damage(hero.attack())
goblin2.take_damage(hero.attack())
hero.take_damage(goblin.attack()) 
hero.take_damage(goblin2.attack())


if __name__ == "__main__":
    main()
