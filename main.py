from farm.animals.chicken import Chicken
from farm.builder import Builder
from farm.visitors.feed_visitor import FeedVisitor
from farm.visitors.mate_visitor import MateVisitor
from farm.visitors.birth_visitor import BirthVisitor
from farm.visitors.speak_visitor import SpeakVisitor

# Create a chicken, cow, and an invalid animal using builder pattern
chicken_builder = Builder()
henrietta = chicken_builder.set_species("Chicken") \
    .set_name("Henrietta") \
    .set_breed("Silkie") \
    .set_age(1) \
    .set_gender("Female") \
    .set_color("White") \
    .set_feather_color("White") \
    .build()

cow_builder = Builder()
bessie = cow_builder.set_species("Cow") \
    .set_name("Bessie") \
    .set_breed("Hereford Cattle") \
    .set_age(5) \
    .set_gender("Male") \
    .set_color("Brown") \
    .set_number_of_horns(2) \
    .build()

# Use visitor pattern to feed, mate, and give birth!

feed_visitor = FeedVisitor()
mate_visitor = MateVisitor()
birth_visitor = BirthVisitor()
speak_visitor = SpeakVisitor()

henrietta.introduce()
henrietta.accept(feed_visitor)
henrietta.accept(mate_visitor)
henrietta.accept(birth_visitor)
henrietta.accept(speak_visitor)

print("---------------------")

bessie.introduce()
bessie.accept(feed_visitor)
bessie.accept(mate_visitor)
bessie.accept(birth_visitor)
bessie.accept(speak_visitor)