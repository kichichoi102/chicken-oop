from farm.domain.single_entities.animal import Animal

class Pig(Animal):
    def __init__(self):
        pass

    def accept(self, visitor) -> None:
        visitor.visit_pig(self)