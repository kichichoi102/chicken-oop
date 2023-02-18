from farm.domain.single_entities.animal import Animal

class Cow(Animal):
    def __init__(self) -> None:
        pass

    def accept(self, visitor) -> None:
        visitor.visit_cow(self)