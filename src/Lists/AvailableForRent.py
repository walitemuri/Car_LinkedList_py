from CarLinkedList.CarLinkedList import CarLinkedList
from NodeTemplates.InStoreCarNode import InStoreCarNode

class AvailableRentList(CarLinkedList):
    """
    Class Template for Available for Rent Linked List
    ...

    Attributes
    ----------
    None
    """
    def __init__(self) -> None:
        super().__init__()
    
    def insertNode (self, plate, mileage) -> None:
        new_node = InStoreCarNode(mileage, plate)
        
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        self.head = self.sortList(self.head)
        return