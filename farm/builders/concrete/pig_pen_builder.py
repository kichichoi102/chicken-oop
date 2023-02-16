
class ConcretePigPenBuilder:

    def __init__(self):
        self.pig_pen = PigPen()

    def build_capacity(self, capacity):
        self.pig_pen.capcity = capacity

    def build_material(self, material):
        self.pig_pen.material = material

    def build_add_animal(self, pig):
        self.pig_pen.add(pig)