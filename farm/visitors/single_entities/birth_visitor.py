from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class BirthVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        return f"{chicken.name} is giving birth!!"

    def visit_cow(self, cow):
        return f"{cow.name} is giving birth!!"

    def visit_pig(self, pig):
        return f"{pig.name} is giving birth!"