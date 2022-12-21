class Car:
    """
    Class to represent a Car Object
    ...

    Attributes
    ----------
    mileage(int):
        Represents how many miles the car has been driven
    plate(str):
        Represents the plate of the car
    """
    def __init__(self, mileage, plate) -> None:
        self.mileage = mileage
        self.plate = plate
