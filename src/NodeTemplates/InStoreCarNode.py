from Car.Car import Car
class InStoreCarNode(Car):
    """
    Class to represent a Car Node within the Available For Rent linked list and the Cars In Repair Linked List

    ...

    Attributes
    ----------
    mileage(int):
        Represents how many miles the car has been driven
    plate(str):
        Represents the plate of the car
    next(node):
        The next car in the list

    Methods
    -------
    None

    """
    def __init__(self, mileage, plate) -> None:
        super().__init__(mileage, plate)
        self.next = None
