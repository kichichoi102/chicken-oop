# Object Oriented Design Used

## Higher Design

### Builders:
The Builder design pattern is a creational pattern used in object-oriented programming to simplify the construction of complex objects. It allows you to separate the construction of an object from its representation, making it easier to create different variations of the object using the same construction process.
#### Components
- Animal Builders: Interfaces that defines the steps required to build an object (single entities).
- Concrete Builders: Classes that implements the Builder interface and provides specific implementations for each of the construction steps.
- Directors: Class that provides a high-level interface for constructing objects using the Builder.
- Product: Animals, Habitats

#### Pros:
1. Encapsulation: The builder pattern allows you to encapsulate the construction of complex objects, making your code more maintainable and easier to understand.
2. Flexible object creation: The builder pattern allows you to create objects with different combinations of properties and attributes, which gives you greater flexibility in object creation.
3. Separation of concerns: The builder pattern separates the construction of an object from its representation, which makes it easier to modify and extend your code without affecting the object's construction.
4. Readable code: The builder pattern results in code that is easier to read and understand, which makes it easier for other developers to work on your codebase.

#### Cons:
1. Overhead: The builder pattern can add some overhead to your code, especially if you have many properties and attributes to set for an object.
2. Complexity: The builder pattern can add complexity to your code, especially if you have many variations of the same object to build.
3. Increased code size: The builder pattern can result in larger code size, which may not be ideal for performance-critical applications.
4. Additional development time: The builder pattern requires you to create a separate builder class for each object you want to build, which can increase development time.

### Visitors:
The Visitor design pattern is a behavioral pattern in object-oriented programming that allows you to add new operations to an object structure without changing the objects themselves. It separates the algorithm from the object structure on which it operates, making it possible to add new operations to the structure without modifying its classes.

#### Pros:
1. Separation of concerns: The visitor pattern separates the behavior of an object from its structure, which makes it easier to modify and extend your code without affecting the object's structure.
2. Improved extensibility: The visitor pattern makes it easier to add new behaviors to an object without modifying the object itself.
3. Improved maintainability: The visitor pattern results in code that is easier to maintain and understand, which makes it easier for other developers to work on your codebase.
4. Improved flexibility: The visitor pattern provides a way to add new operations to an object hierarchy without modifying the hierarchy.

#### Cons:
1. Complexity: The visitor pattern can add complexity to your code, especially if you have a large number of objects to operate on.
2. Increased code size: The visitor pattern can result in larger code size, which may not be ideal for performance-critical applications.
3. Reduced encapsulation: The visitor pattern requires the object hierarchy to expose its internal structure to the visitor, which can reduce the encapsulation of the object hierarchy.
4. Additional development time: The visitor pattern requires you to create a separate visitor class for each operation you want to perform on an object hierarchy, which can increase development time.

## Shared Design

### Domain Entities:
- Single Entities: Contains animals such as Chicken, Cow, Pig
- Collections: Contains habitats, Chicken Coop, Cow Pen, Pig Pen

### Interfaces
- Animals: Abstract base super classes that single entities inherit from
- Habitats: Abstract base super classes that collective entities inherit from