from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class FeedVisitor(AnimalVisitor):
    def visit_chicken(self, chicken):
        return f"Feeding chicken {chicken.name}"

    def visit_cow(self, cow):
        return f"Feeding cow {cow.name}"

    def visit_pig(self, pig):
        return f"Feeding pig {pig.name}"