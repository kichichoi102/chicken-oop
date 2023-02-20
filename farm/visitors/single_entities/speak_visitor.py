from farm.visitors.interfaces.animal_visitor import AnimalVisitor
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class SpeakVisitor(AnimalVisitor):
    def visit_chicken(self, chicken:Chicken) -> str:
        return "Cock-a-doodle-doo!!"

    def visit_cow(self, cow:Cow) -> str:
        return "Moooooooo"

    def visit_pig(self, pig:Pig) -> str:
        return "Oink Oink"
