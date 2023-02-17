from typing import List

from farm.domain.collections.habitat import Habitat
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.animal import Animal

class ChickenCoop(Habitat):
    def __init__(self) -> None:
        self.chickens: List[Chicken] = []

    # Liskov Substitution Principle
    # talking point hehe
    def add(self, chicken: Chicken) -> None:
        self.chickens.append(chicken)

    # Liskov Substitution Principle
    def get_animals(self) -> List[Chicken]:
        return self.chickens