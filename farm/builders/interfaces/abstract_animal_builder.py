from abc import ABC, abstractmethod

class AbstractAnimalBuilder(ABC):

    @abstractmethod
    def build_species(self, species:str) -> None:
        pass

    @abstractmethod
    def build_name(self, name:str) -> None:
        pass

    @abstractmethod
    def build_age(self, age:int) -> None:
        pass

    @abstractmethod
    def build_gender(self, gender:str) -> None:
        pass
        
    @abstractmethod
    def build_color(self, color:str) -> None:
        pass

    @abstractmethod
    def build_weight(self, weight:int) -> None:
        pass

    @abstractmethod
    def return_animal(self) -> None:
        pass
    