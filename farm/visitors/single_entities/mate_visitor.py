from farm.visitors.interfaces.animal_visitor import AnimalVisitor
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class MateVisitor(AnimalVisitor):
    def visit_chicken(self, chicken:Chicken) -> str:
        return f"Mating chicken {chicken.name}"

    def visit_cow(self, cow:Cow) -> str:
        return f"Mating cow {cow.name}"

    def visit_pig(self, pig:Pig) -> str:
        return f"Mating pig {pig.name}"
