from farm.animals.animal import Animal

class Chicken(Animal):
    def __init__(self, species, breed, name, age, gender, color, feather_color):
        super().__init__(species, breed, name, age, gender, color)
        self.feather_color = feather_color

    def accept(self, visitor):
        visitor.visit_chicken(self)