class AnimalHabitatDirector:

    def __init__(self, builder):
        self.builder = builder

    def build_habitat(self, capacity, material):
        self.builder.build_capacity(capacity)
        self.builder.build_material(material)

    def add_animal(self, **kwargs):
        animal_builder = kwargs['animal_builder']
        animal_builder.build_species(kwargs["species"])
        animal_builder.build_name(kwargs["name"])
        animal_builder.build_weight(kwargs["weight"])

        self.builder.build_add_animal(animal_builder.chicken)

    def get_habitat(self):
        return self.builder.get_habitat()