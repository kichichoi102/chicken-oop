from abc import ABC, abstractmethod

class Habitat(ABC):
    
    @abstractmethod
    def __init__(self, animal):
        pass

    @abstractmethod
    def add(self, animal):
        pass

    @abstractmethod
    def get_animals(self):
        pass