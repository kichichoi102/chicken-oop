from farm.visitors.interfaces.animal_visitor import AnimalVisitor
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class FeedVisitor(AnimalVisitor):
    def visit_chicken(self, chicken) -> str:
        return f"Feeding chicken {chicken.name}"

    def visit_cow(self, cow) -> str:
        return f"Feeding cow {cow.name}"

    def visit_pig(self, pig) -> str:
        return f"Feeding pig {pig.name}"