from Car import Car
class NodeTypeTwo(Car):
    """
    Class to represent a Car Node within the Rented linked list, includes expected return date

    ...

    Attributes
    ----------
    mileage(int):
        Represents how many miles the car has been driven
    plate(str):
        Represents the plate of the car
    next(node):
        The next car in the list
    expectedReturn(str):
        The expected return date of the car represented as a String in the format "YYMMDD"

    Methods
    -------
    None

    """
    def __init__(self, mileage, plate, expectedReturn) -> None:
        super().__init__(mileage, plate)
        self.next = None
        self.expectedReturn = expectedReturn
