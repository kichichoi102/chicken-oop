import pytest
from farm.domain.single_entities.chicken import Chicken
from farm.visitors.single_entities.birth_visitor import BirthVisitor
from farm.visitors.single_entities.feed_visitor import FeedVisitor
from farm.visitors.single_entities.mate_visitor import MateVisitor
from farm.visitors.single_entities.speak_visitor import SpeakVisitor

@pytest.fixture
def chicken():
    chicken = Chicken()
    chicken.name = "Henrietta"
    return chicken

@pytest.fixture
def birth_visitor():
    return BirthVisitor()

@pytest.fixture
def feed_visitor():
    return FeedVisitor()

@pytest.fixture
def mate_visitor():
    return MateVisitor()

@pytest.fixture
def speak_visitor():
    return SpeakVisitor()

def test_can_instantiate():
    chicken = Chicken()
    assert isinstance(chicken, Chicken)

def test_can_birth(chicken, birth_visitor):
    birth_string = chicken.accept(birth_visitor)
    assert birth_string == "Henrietta is giving birth!!"

def test_can_feed(chicken, feed_visitor):
    feed_string = chicken.accept(feed_visitor)
    assert feed_string == "Feeding chicken Henrietta"

def test_can_mate(chicken, mate_visitor):
    mate_string = chicken.accept(mate_visitor)
    assert mate_string == "Mating chicken Henrietta"

def test_can_speak(chicken, speak_visitor):
    speak_string = chicken.accept(speak_visitor)
    assert speak_string == "Cock-a-doodle-doo!!"
