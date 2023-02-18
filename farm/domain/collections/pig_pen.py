from typing import List

from farm.domain.collections.habitat import Habitat
from farm.domain.single_entities.pig import Pig
from farm.domain.single_entities.animal import Animal

class PigPen(Habitat):
    def __init__(self) -> None:
        self.pigs: List[Pig] = []

    # Liskov Substitution Principle
    def add(self, pig: Pig) -> None:
        self.pigs.append(pig)

    # Liskov Substitution Principle
    def get_animals(self) -> List[Pig]:
        return self.pigs
