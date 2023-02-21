# Object Oriented Design Used

## Higher Design

### Builders:
The Builder design pattern is a creational pattern used in object-oriented programming to simplify the construction of complex objects. It allows you to separate the construction of an object from its representation, making it easier to create different variations of the object using the same construction process.
- Animal Builders: Interfaces that defines the steps required to build an object (single entities).
- Concrete Builders: Classes that implements the Builder interface and provides specific implementations for each of the construction steps.
- Directors: Class that provides a high-level interface for constructing objects using the Builder.
- Product: Animals, Habitats

### Visitors:
The Visitor design pattern is a behavioral pattern in object-oriented programming that allows you to add new operations to an object structure without changing the objects themselves. It separates the algorithm from the object structure on which it operates, making it possible to add new operations to the structure without modifying its classes.

## Shared Design

### Domain Entities:
- Single Entities: Contains animals such as Chicken, Cow, Pig
- Collections: Contains habitats, Chicken Coop, Cow Pen, Pig Pen

### Interfaces
- Animals: Abstract base super classes that single entities inherit from
- Habitats: Abstract base super classes that collective entities inherit from