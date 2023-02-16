class MateVisitor:
    def visit_chicken(self, chicken):
        print(f"Mating chicken {chicken.name}")

    def visit_cow(self, cow):
        print(f"Mating cow {cow.name}")
