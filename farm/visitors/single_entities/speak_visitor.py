from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class SpeakVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        print("Cock-a-doodle-doo!!")

    def visit_cow(self, cow):
        print("Moooooooo")

    def visit_pig(self, pig):
        print("Oink Oink")