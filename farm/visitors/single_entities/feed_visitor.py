from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class FeedVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        print(f"Feeding chicken {chicken.name}")

    def visit_cow(self, cow):
        print(f"Feeding cow {cow.name}")

    def visit_pig(self, pig):
        print(f"Feeding pig {pig.name}")