from abc import ABC, abstractmethod

class AbstractAnimalBuilder(ABC):

    @abstractmethod
    def build_species(self, species):
        pass

    @abstractmethod
    def build_name(self, name):
        pass

    @abstractmethod
    def build_age(self, age):
        pass

    @abstractmethod
    def build_gender(self, gender):
        pass
        
    @abstractmethod
    def build_color(self, color):
        pass

    @abstractmethod
    def build_weight(self, weight):
        pass
    