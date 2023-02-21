# OOP Pillars

## 1. Inheritance
AbstractBaseClasses: 
- animals and habitats inherit from base classes.

## 2. Polymorphism
- Single Entities are subclasses of Animal classes
- Collection Entities are subclasses of Habitat classes
- Builder classes are subclasses of abstract animal builder
- Concrete Builder classes are subclasses of abstract habitat builder

## 3. Abstraction
- Collections manages collection of single entities
- eg: Chicken coop contains instances of chicken class
- Hides implementation of how Chicken objects are stored adn accessed

## 4. Encapsulation
- Builders/concrete encapsulate the attributes of single entities/collections respectively to set/build their attributes
- Visitors encapsulates the methods of entities.

## 5. Composition
- Used composition to model the relationship between a Chicken object and its Coop object. 
- Eg. The Coop object has a maximum capacity, and the Chicken object has a reference to the Coop object it belongs to. 

## 6. Interfaces
- Abstract Base Classes that subclasses implement

