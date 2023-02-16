
class ConcreteCowPenBuilder:
    def __init__(self):
        self.cow_pen = CowPen()

    def build_capacity(self, capacity):
        self.cow_pen.capcity = capacity

    def build_material(self, material):
        self.cow_pen.material = material

    def build_add_animal(self, cow):
        self.cow_pen.add(cow)