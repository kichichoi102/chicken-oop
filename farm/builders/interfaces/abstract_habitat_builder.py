from abc import ABC, abstractmethod
from farm.domain.single_entities.animal import Animal

class AbstractHabitatBuilder(ABC):
    
    @abstractmethod
    def build_capacity(self, capacity: int) -> None:
        pass

    @abstractmethod
    def build_material(self, material: str) -> None:
        pass

    @abstractmethod
    def build_add_animal(self, animal: Animal) -> None:
        pass

    @abstractmethod
    def get_habitat(self) -> None:
        pass