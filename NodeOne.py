
class NodeTypeOne:
    """
    Class to represent the car within the Available For Rent linked list and the Cars In Repair Linked List

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
        self.mileage = mileage
        self.plate = plate
        self.next = None



class AvailableRent:
    def __init__(self) -> None:
        self.head = None
    
    def printList(self) -> None:
        temp = self.head
        while(temp):
            print(temp.plate)
            temp = temp.next


class RentedList(AvailableRent):
    pass

class RepairList(AvailableRent):
    pass

