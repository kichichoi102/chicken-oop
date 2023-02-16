from abc import ABC, abstractmethod

class AbstractHabitatBuilder(ABC):
    
    @abstractmethod
    def build_capacity(self):
        pass

    @abstractmethod
    def build_material(self):
        pass

    @abstractmethod
    def build_add_animal(self):
        pass
