from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class SpeakVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        return "Cock-a-doodle-doo!!"

    def visit_cow(self, cow):
        return "Moooooooo"

    def visit_pig(self, pig):
        return "Oink Oink"
