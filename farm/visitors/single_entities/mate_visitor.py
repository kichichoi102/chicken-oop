from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class MateVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        return f"Mating chicken {chicken.name}"

    def visit_cow(self, cow):
        return f"Mating cow {cow.name}"

    def visit_pig(self, pig):
        return f"Mating pig {pig.name}"
