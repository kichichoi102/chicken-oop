from farm.domain.interfaces.animal import Animal

class Pig(Animal):
    """
    Pig Class

    Extends Abstract Animal Class

    Arguments:
        Animal -- Animal Abstract Class
    """
    def __init__(self):
        pass

    def accept(self, visitor) -> None:
        """
        accept visitor interface method

        Takes in a visitor instance to run the incoming
        visitor methods

        Arguments:
            visitor -- Visitor
        """
        visitor.visit_pig(self)