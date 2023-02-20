import pytest
from farm.domain.single_entities.pig import Pig
from farm.visitors.single_entities.birth_visitor import BirthVisitor
from farm.visitors.single_entities.feed_visitor import FeedVisitor
from farm.visitors.single_entities.mate_visitor import MateVisitor
from farm.visitors.single_entities.speak_visitor import SpeakVisitor

@pytest.fixture
def pig():
    pig = Pig()
    pig.name = "Mimi"
    return pig

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
    pig = Pig()
    assert isinstance(pig, Pig)

def test_can_birth(pig, birth_visitor):
    birth_string = pig.accept(birth_visitor)
    assert birth_string == "Mimi is giving birth!"

def test_can_feed(pig, feed_visitor):
    feed_string = pig.accept(feed_visitor)
    assert feed_string == "Feeding pig Mimi"

def test_can_mate(pig, mate_visitor):
    mate_string = pig.accept(mate_visitor)
    assert mate_string == "Mating pig Mimi"

def test_can_speak(pig, speak_visitor):
    speak_string = pig.accept(speak_visitor)
    assert speak_string == "Oink Oink"