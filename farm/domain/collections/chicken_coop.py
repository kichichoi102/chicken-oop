from farm.domain.collections.habitat import Habitat

class ChickenCoop(Habitat):
    def __init__(self):
        self.chickens = []

    def add(self, chicken):
        self.chickens.append(chicken)

    def get_animals(self):
        return self.chickens