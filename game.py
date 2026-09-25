from goblin import Goblin
from hero import Hero
from wizard import Wizard
from boss import Boss
ARENA_NAME = "The Trip T Tower"

def  battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

        if hero.is_alive():
            print(f"{hero.name} wins!")
        else:
            print(f"{enemy.name} wins!")


        




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
battle(hero,goblin)
battle(hero,goblin2)

bossguy = Boss("Devin")
battle(hero, bossguy)

if __name__ == "__main__":
    main()
