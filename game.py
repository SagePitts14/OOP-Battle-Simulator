from goblin import Goblin


ARENA_NAME = "The Iron Rectangle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("D0rian")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    goblin = Goblin("Ahstung")
    
    print(f"{goblin.name} enters the arena with {goblin.health} health.")


if __name__ == "__main__":
    main()
