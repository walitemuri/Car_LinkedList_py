from CarLinkedList.CarLinkedList import CarLinkedList
from RentedCarNode import RentedCarNode
from datetime import datetime as dt
class RentedList(CarLinkedList):
    def __init__(self) -> None:
        super().__init__()

    def insertNode (self, plate, mileage, expectedReturn) -> None:
        new_node = RentedCarNode(mileage, plate, expectedReturn)
        a = dt.strptime(expectedReturn, "%Y-%m-%d")

        if self.head is None:
            self.head = new_node
            return
        elif dt.strptime(self.head.expectedReturn,"%Y-%m-%d") >= a:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None and dt.strptime(temp.next.expectedReturn, "%Y-%m-%d") < a:
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node
        return

    # def deleteNode(self, target) -> None:
        temp = self.head

        if (temp is None):
            print("Empty List")
            return

        if(temp.plate == target):
            self.head = temp.next
            return

        while temp.plate is not target and temp is not None:
            temp = temp.next
        
        if(temp is None):
            return
        else:
            prev = temp
            temp = temp.next.next
            prev.next = temp
        return