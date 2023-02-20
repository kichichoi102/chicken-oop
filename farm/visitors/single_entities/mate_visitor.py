from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class MateVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        print(f"Mating chicken {chicken.name}")

    def visit_cow(self, cow):
        print(f"Mating cow {cow.name}")

    def visit_pig(self, pig):
        print(f"Mating pig {pig.name}")
