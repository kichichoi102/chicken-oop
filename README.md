# chicken-oop
Based on OOP oriented concepts in Python I should create a model (python script) of a chicken.

## Project Report
[Chicken OOP - Google Doc](https://docs.google.com/document/d/1d3POQjeTx4FpnYwPIogbDZY74NMiMPsBaIAlBNu410I/edit?usp=sharing)

## Dev Dependencies

### Setup.py (Optional):
- Dependencies: setuptools, wheel
- `python setup.py sdist bdist_wheel`

### Pylint:
- Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for bad code smells. 
- `pylint <path_to_file>`

### Mypy:
- Mypy is a static type checker for Python.
- type hints according to PEP 484
- `mypy --strict --enable-incomplete-feature=Unpack <path_to_file>`


## Usage - Python
```bash
<!-- Make Virtual Environment -->
~/chicken-oop$ mkdir venv
~/chicken-oop$ cd venv
~/chicken-oop$ py -3.7 -m venv venv
~/chicken-oop$ source venv/bin/activate
<!-- Install Requirements -->
~/chicken-oop$ pip install -r requirements.txt
<!-- Run Validations and Tests -->
~/chicken-oop$ pylint ./farm
~/chicken-oop$ mypy --strict --enable-incomplete-feature=Unpack ./farm
~/chicken-oop$ pytest
<!-- Run Main -->
~/chicken-oop$ python3 main.py
```

## Usage Docker
```bash
~/chicken-oop$ docker build -t <image_name> .
~/chicken-oop$ docker run --rm -it <image_name>
```

## Expected Output
```python
Chicken Coop:
Capacity: 10
Material: Wood
Number: 2
Animals: ['Henrietta', 'Clucky']


Cow Pen:
Capacity: 20
Material: Metal
Number: 1
Animals: ['Bessie']


Pig Pen:
Capacity: 5
Material: Oak Wood
Number: 1
Animals: ['Mimi']
```

## OOP Design Patterns

### Builder:
The builder design pattern is a creational pattern used in software development to create complex objects with many configurable attributes. 

### Visitor:
The visitor design pattern is a behavioral pattern used in software development to separate algorithmic operations from the objects on which they operate.


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