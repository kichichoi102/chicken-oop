from farm.animals.animal import Animal

class Cow(Animal):
    def __init__(self, species, breed, name, age, gender, color, number_of_horns):
        super().__init__(species, breed, name, age, gender, color)
        self.number_of_horns = number_of_horns

    def accept(self, visitor):
        visitor.visit_cow(self)