from farm.domain.single_entities.animal import Animal

class Chicken(Animal):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visit_chicken(self)