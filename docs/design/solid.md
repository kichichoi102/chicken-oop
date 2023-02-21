# SOLID Principles Used

## Single Responsibility
- Achieved by Visitor Pattern.
- Each method/visitor class has a clear responsibility:
- Eg. Collections: `add`, `get_animals_by_name`, etc
- Eg. Single Entities: `birth`, `feed`, etc
- Furthermore, All entity, builder, and domain have singular reponsibilities.

## Open/Closed
- Can extend builders and domains by creating sub classes
- Eg. `abstract_animal/habitat_builder`, `animal/habitat_visitor`, `animal/habitat`
- These abstract classes are extensions of ABC python module, and their respective methods are abstract methods.

## Liskov Substitution
- All actionable classes are subclasses of abstract classes outlined in `Open/Closed` section

## Interface Segregation
- Different interfaces between animals and habitats and visitors.

## Dependency Inversion
- All high level modules don't depend on low-level modules, rather depend on abstractions!
