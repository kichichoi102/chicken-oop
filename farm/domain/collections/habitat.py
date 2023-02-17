from typing import List
from abc import ABC, abstractmethod

from farm.domain.single_entities.animal import Animal

class Habitat(ABC):
    
    @abstractmethod
    def __init__(self, animal:Animal) -> None:
        pass

    @abstractmethod
    def add(self, animal:Animal) -> None:
        pass

    @abstractmethod
    def get_animals(self) -> List[Animal]:
        pass