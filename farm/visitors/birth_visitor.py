class BirthVisitor:
    def visit_chicken(self, chicken):
        print(f"{chicken.name} is giving birth!!")

    def visit_cow(self, cow):
        print(f"{cow.name} is giving birth!!")