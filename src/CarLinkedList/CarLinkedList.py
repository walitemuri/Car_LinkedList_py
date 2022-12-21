from InStoreCarNode import InStoreCarNode
from RentedCarNode import RentedCarNode
from typing import Union

class CarLinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def printList(self) -> None:
        temp = self.head
        while(temp):
            print(temp.plate)
            temp = temp.next
    
    def insertNode (self, plate, mileage) -> None:
        new_node = InStoreCarNode(mileage, plate)
        
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        return
        
    def __sortedMerge(self, a, b) -> InStoreCarNode:
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.mileage <= b.mileage:
            result = a
            result.next = self.__sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.__sortedMerge(a, b.next)
        return result

    def __getMiddle (self, head) -> InStoreCarNode:
        if head is None:
            return head
        
        slow = head
        fast = head

        while(fast.next is not None and 
            fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def __mergeSort(self, h) -> InStoreCarNode:
        if h is None or h.next is None:
            return h

        middle = self.__getMiddle(h)
        next_to_mid = middle.next

        middle.next = None
        left = self.__mergeSort(h)
        right = self.__mergeSort(next_to_mid)

        sorted_list = self.__sortedMerge(left, right)
        return sorted_list
    
    def sortList (self, head) -> InStoreCarNode:
        new_head = self.__mergeSort(head)
        return new_head

    def deleteNode (self, target) -> None:      
        temp = self.head

        if (temp is None):
            print("Empty List")
            return

        if(temp.plate is target):
            self.head = temp.next
            temp = None
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

    def searchTree (self, target) -> Union[InStoreCarNode, RentedCarNode]:
        temp = self.head

        while(temp is not None):
            if(temp.plate == target):
                return temp
            temp = temp.next
            
        return None