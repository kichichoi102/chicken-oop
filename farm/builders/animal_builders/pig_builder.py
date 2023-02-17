
class PigBuilder(AbstractAnimalBuilder):

    def __init__(self):
        self.pig = Pig()

    def build_species(self, species):
        self.pig.species = species

    def build_weight(self, weight):
        self.pig.species = weight
    
    def build_sound(self, sound):
        self.pig.sound = sound
