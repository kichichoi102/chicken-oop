class Animal:
    def __init__(self, species, breed, name, age, gender, color):
        self.species = species
        self.breed = breed
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color

    def introduce(self):
        print(f"Hi there! my name is {self.name}, and I am a {self.age} year old {self.species}!")
