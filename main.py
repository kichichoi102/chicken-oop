# from farm.domain.single_entities.chicken import Chicken
# from farm.builder import Builder
# from farm.visitors.feed_visitor import FeedVisitor
# from farm.visitors.mate_visitor import MateVisitor
# from farm.visitors.birth_visitor import BirthVisitor
# from farm.visitors.speak_visitor import SpeakVisitor

from farm.builders.animal_builders.chicken_builder import ChickenBuilder
from farm.builders.animal_builders.cow_builder import CowBuilder
from farm.builders.animal_builders.pig_builder import PigBuilder

from farm.builders.concrete.chicken_coop_builder import ConcreteChickenCoopBuilder
from farm.builders.concrete.cow_pen_builder import ConcreteCowPenBuilder
from farm.builders.concrete.pig_pen_builder import ConcretePigPenBuilder

from farm.builders.directors.animal_habitat_director import AnimalHabitatDirector

from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.collections.cow_pen import CowPen
from farm.domain.collections.pig_pen import PigPen

# Instantiate a chicken, cow, and pig using builder pattern
chicken_builder = ChickenBuilder()
cow_builder = CowBuilder()
pig_builder = PigBuilder()

# Instantiate concrete habitat builders
chicken_coop_builder = ConcreteChickenCoopBuilder()
cow_pen_builder = ConcreteCowPenBuilder()
pig_pen_builder = ConcretePigPenBuilder()

# Instantiate Directors and create habitats
chicken_coop_director = AnimalHabitatDirector(chicken_coop_builder)
chicken_coop_director.build_habitat(10, "Wood")
cow_pen_director = AnimalHabitatDirector(cow_pen_builder)
cow_pen_director.build_habitat(20, "Metal")
pig_pen_director = AnimalHabitatDirector(pig_pen_builder)
pig_pen_director.build_habitat(5, "Oak Wood")

# Add animals to respective Habitats
# Chickens, Henrietta and Clucky
chicken_coop_director.add_animal(
    animal_builder=chicken_builder, 
    name="Henrietta", 
    species="Chicken", 
    weight=10, 
    sound="cockadoodledoo1"
)
# Create new instance of Animal (Chicken)
chicken_builder.__init__()
chicken_coop_director.add_animal(
    animal_builder=chicken_builder, 
    name="Clucky", 
    species="Chicken", 
    weight=11, 
    sound="cockadoodledoo2"
)

# Add Cow, Bessie
cow_pen_director.add_animal(
    animal_builder=cow_builder, 
    name="Bessie", 
    species="Cow", 
    weight=100, 
    sound="Moo"
)

# Add Pig, Mimi
pig_pen_director.add_animal(
    animal_builder=pig_builder, 
    name="Mimi", 
    species="Pig", 
    weight=50, 
    sound="pig_sound"
)

# Get Habitat Info
chicken_coop = chicken_coop_director.get_habitat()
cow_pen = cow_pen_director.get_habitat()
pig_pen = pig_pen_director.get_habitat()

print(chicken_coop)
print(cow_pen)
print(pig_pen)

# Create a chicken, cow, and an invalid animal using builder pattern
# chicken_builder = Builder()
# henrietta = chicken_builder.set_species("Chicken") \
#     .set_name("Henrietta") \
#     .set_breed("Silkie") \
#     .set_age(1) \
#     .set_gender("Female") \
#     .set_color("White") \
#     .set_feather_color("White") \
#     .build()

# cow_builder = Builder()
# bessie = cow_builder.set_species("Cow") \
#     .set_name("Bessie") \
#     .set_breed("Hereford Cattle") \
#     .set_age(5) \
#     .set_gender("Male") \
#     .set_color("Brown") \
#     .set_number_of_horns(2) \
#     .build()

# Use visitor pattern to feed, mate, and give birth!

# feed_visitor = FeedVisitor()
# mate_visitor = MateVisitor()
# birth_visitor = BirthVisitor()
# speak_visitor = SpeakVisitor()

# henrietta.introduce()
# henrietta.accept(feed_visitor)
# henrietta.accept(mate_visitor)
# henrietta.accept(birth_visitor)
# henrietta.accept(speak_visitor)

# print("---------------------")

# bessie.introduce()
# bessie.accept(feed_visitor)
# bessie.accept(mate_visitor)
# bessie.accept(birth_visitor)
# bessie.accept(speak_visitor)
