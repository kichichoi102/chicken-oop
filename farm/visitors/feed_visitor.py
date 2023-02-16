class FeedVisitor:
    def visit_chicken(self, chicken):
        print(f"Feeding chicken {chicken.name}")

    def visit_cow(self, cow):
        print(f"Feeding cow {cow.name}")