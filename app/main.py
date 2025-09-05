class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        if self.health > 0:
            Animal.alive.append(self)
        self.hidden = False

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        predator = next((a for a in Animal.alive
                         if isinstance(a, Carnivore)), None)
        if (predator and isinstance(herbivore, Herbivore)
                and not herbivore.hidden):
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()
