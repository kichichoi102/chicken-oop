from farm.visitors.interfaces.animal_visitor import AnimalVisitor
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class BirthVisitor(AnimalVisitor):
    def visit_chicken(self, chicken:Chicken) -> str:
        return f"{chicken.name} is giving birth!!"

    def visit_cow(self, cow:Cow) -> str:
        return f"{cow.name} is giving birth!!"

    def visit_pig(self, pig:Pig) -> str:
        return f"{pig.name} is giving birth!"