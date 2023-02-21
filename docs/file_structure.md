# File Structure

## File Directories
```bash
.
└── .
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── docs
    │   ├── README.md
    │   ├── conventions
    │   │   ├── README.md
    │   │   ├── pep_257_docstring.md
    │   │   ├── pep_484_type_hints.md
    │   │   └── pep_8_style_guide.md
    │   ├── design
    │   │   ├── object_oriented_design.md
    │   │   ├── object_oriented_programming.md
    │   │   └── solid.md
    │   ├── file_structure.md
    │   └── tests
    │       └── README.md
    ├── farm
    │   ├── builders
    │   │   ├── animal_builders
    │   │   │   ├── chicken_builder.py
    │   │   │   ├── cow_builder.py
    │   │   │   └── pig_builder.py
    │   │   ├── concrete
    │   │   │   ├── chicken_coop_builder.py
    │   │   │   ├── cow_pen_builder.py
    │   │   │   └── pig_pen_builder.py
    │   │   ├── directors
    │   │   │   └── animal_habitat_director.py
    │   │   └── interfaces
    │   │       ├── abstract_animal_builder.py
    │   │       ├── abstract_habitat_builder.py
    │   │       └── request_params.py
    │   ├── domain
    │   │   ├── __init__.py
    │   │   ├── collections
    │   │   │   ├── chicken_coop.py
    │   │   │   ├── cow_pen.py
    │   │   │   └── pig_pen.py
    │   │   ├── interfaces
    │   │   │   ├── animal.py
    │   │   │   └── habitat.py
    │   │   └── single_entities
    │   │       ├── chicken.py
    │   │       ├── cow.py
    │   │       └── pig.py
    │   ├── exceptions
    │   │   ├── capacity_full_error.py
    │   │   └── not_found_error.py
    │   └── visitors
    │       ├── __init__.py
    │       ├── collections
    │       │   ├── add_visitor.py
    │       │   ├── get_animal_by_name_visitor.py
    │       │   └── get_animals_visitor.py
    │       ├── interfaces
    │       │   ├── animal_visitor.py
    │       │   └── habitat_visitor.py
    │       └── single_entities
    │           ├── birth_visitor.py
    │           ├── feed_visitor.py
    │           ├── mate_visitor.py
    │           └── speak_visitor.py
    ├── main.py
    ├── pull_request_template.md
    ├── setup.py
    └── tests
        ├── __init__.py
        └── farm
            ├── __init__.py
            ├── builders
            │   ├── __init__.py
            │   ├── animal_builders
            │   │   ├── __init__.py
            │   │   ├── test_chicken_builder.py
            │   │   ├── test_cow_builder.py
            │   │   └── test_pig_builder.py
            │   ├── concrete
            │   │   ├── __init__.py
            │   │   ├── test_chicken_coop_builder.py
            │   │   ├── test_cow_pen_builder.py
            │   │   └── test_pig_pen_builder.py
            │   ├── directors
            │   │   └── test_animal_habitat_director.py
            │   └── interfaces
            │       ├── __init__.py
            │       ├── test_abstract_animal_builder.py
            │       └── test_abstract_habitat_builder.py
            └── domain
                ├── __init__.py
                ├── collections
                │   ├── __init__.py
                │   ├── test_chicken_coop.py
                │   ├── test_cow_pen.py
                │   └── test_pig_pen.py
                ├── interfaces
                │   ├── __init__.py
                │   ├── test_animal.py
                │   └── test_habitat.py
                └── single_entities
                    ├── __init__.py
                    ├── test_chicken.py
                    ├── test_cow.py
                    └── test_pig.py
```
