import pytest
from farm.domain.single_entities.cow import Cow
from farm.visitors.single_entities.birth_visitor import BirthVisitor
from farm.visitors.single_entities.feed_visitor import FeedVisitor
from farm.visitors.single_entities.mate_visitor import MateVisitor
from farm.visitors.single_entities.speak_visitor import SpeakVisitor

@pytest.fixture
def cow():
    cow = Cow()
    cow.name = "Bessie"
    return cow

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
    cow = Cow()
    assert isinstance(cow, Cow)

def test_can_birth(cow, birth_visitor):
    birth_string = cow.accept(birth_visitor)
    assert birth_string == "Bessie is giving birth!!"

def test_can_feed(cow, feed_visitor):
    feed_string = cow.accept(feed_visitor)
    assert feed_string == "Feeding cow Bessie"

def test_can_mate(cow, mate_visitor):
    mate_string = cow.accept(mate_visitor)
    assert mate_string == "Mating cow Bessie"

def test_can_speak(cow, speak_visitor):
    speak_string = cow.accept(speak_visitor)
    assert speak_string == "Moooooooo"