from NodeOne import NodeTypeOne
class AvailableRent:
    def __init__(self) -> None:
        self.head = None
    
    def printList(self) -> None:
        temp = self.head
        while(temp):
            print(temp.plate)
            temp = temp.next
    
    def insertNode (self, plate, mileage) -> None:
        new_node = NodeTypeOne(mileage, plate)
        
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new_node
        return
        
    def __sortedMerge(self, a, b) -> NodeTypeOne:
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

    def __getMiddle (self, head) -> NodeTypeOne:
        if head is None:
            return head
        
        slow = head
        fast = head

        while(fast.next is not None and 
            fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def mergeSort(self, h) -> NodeTypeOne:
        if h is None or h.next is None:
            return h

        middle = self.__getMiddle(h)
        next_to_mid = middle.next

        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(next_to_mid)

        sorted_list = self.__sortedMerge(left, right)
        return sorted_list
    
    def sortList (self, head) -> NodeTypeOne:
        new_head = self.mergeSort(head)
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

        while temp.next.plate is not target and temp is not None:
            temp = temp.next
        
        if(temp is None):
            return
        else:
            prev = temp
            temp = temp.next.next
            prev.next = temp
        return
