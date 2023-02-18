from typing import List

from farm.domain.collections.habitat import Habitat
from farm.domain.single_entities.cow import Cow

class CowPen(Habitat):
    def __init__(self) -> None:
        self.cows: List[Cow] = []

    # Liskov Substitution Principle
    def add(self, cow: Cow) -> None:
        self.cows.append(cow)

    # Liskov Substitution Principle
    def get_animals(self) -> List[Cow]:
        return self.cows