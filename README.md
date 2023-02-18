# chicken-oop
Based on OOP oriented concepts in Python I should create a model (python script) of a chicken.

## [TODO]
1. Add docstrings
2. add tests
3. add methods to get animals in habitat by name
4. implement visitors in builder
5. add documentation directory with diagrams
6. add doc with patterns, reasoning, diagrams, etc

[TODO] add doc of WHY i did builder + visitor

## OOP Design Patterns
### Visitor:
chicken - domain class
if feed, mate was part of chicken class, 
 - adds coupling to domain and actions
 - can add actions without interfering the other class

### Builder:
 - can add new attributes quickly

### Interfaces:
 - [TODO] add details here

## Dependencies

### Setup.py:
- Dependencies: setuptools, wheel
- `python setup.py sdist bdist_wheel`

### Pylint:
- Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for bad code smells. 
- `pylint <path_to_file>`

### Mypy:
- Mypy is a static type checker for Python.
- type hints according to PEP 484
- `mypy --strict --enable-incomplete-feature=Unpack <path_to_file>`

### Pycodestyle:
- [Not Implemented Yet]
- pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.
- https://github.com/PyCQA/pycodestyle

## FAQs
Q. Is it good practice in python to always include attributes in a class if a have a setter class that creates those attributes?

A. It depends on your specific use case and the design of your class.

If you have a setter method that creates attributes when they are not already present, it may not be necessary to always include those attributes in the class definition. This can make your code more flexible and allow for attributes to be added dynamically as needed.

However, if you have certain attributes that are essential to the functionality of your class, it may be a good idea to include them in the class definition, even if they can also be created using a setter method. This can help make the code more readable and make it clear what attributes are expected to be present.

Ultimately, the decision of whether to always include attributes in a class or to dynamically create them using a setter method depends on the specific requirements and constraints of your project, and the trade-offs between flexibility, readability, and maintainability.

Post Script: For single entity and collective classes (Animals + Habitats respectively), I decided NOT to add attributes to them to make these classes more extensible. Instead if I need to add new attributes, I will add them to setter methods (outlined in build service). This is one of the fundamental principles of the Builder Pattern, extensibility.

Q. Incompatible overrides

A. It’s unsafe to override a method with a more specific argument type, as it violates the Liskov substitution principle. For return types, it’s unsafe to override a method with a more general return type. 
eg.
Wrong: ChickenCoop.get_animals(self) -> List[Animals]
Correct: ChickenCoop.get_animals(self) -> List[Chickens]