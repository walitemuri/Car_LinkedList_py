from AvailableForRent import AvailableRentList
from Rented import RentedList
from InRepair import RepairList
from Interface import Interface

class CarRental:
    def __init__(self) -> None:
        self.avRentList = AvailableRentList()
        self.rentedList = RentedList()
        self.repairList = RepairList()
        self.interface = Interface()
    
    def addReturnedCarToAvailableList(self, carPlate, mileage) -> None:
        is_valid_input = self.rentedList.searchTree(carPlate)

        if is_valid_input is not None:
            self.rentedList.deleteNode(carPlate)
            self.avRentList.insertNode(carPlate, mileage)
        else:
            print("Error: Car is not on list")
        return
    
    def addReturnedCarToRepairList(self, carPlate, mileage) -> None:
        is_valid_input = self.rentedList.searchTree(carPlate)

        if is_valid_input is not None:
            self.rentedList.deleteNode(carPlate)
            self.repairList.insertNode(carPlate, mileage)
        else:
            print("Error: Car not found in list")
        return

    def transferCarFromRepairToAvRentList(self, carPlate) -> None:
        is_valid_input = self.repairList.searchTree(carPlate)

        if is_valid_input is not None:
            self.repairList.deleteNode(is_valid_input.plate)
            self.avRentList.insertNode(is_valid_input.plate, is_valid_input.mileage)
        else:
            print("Error: Car not found on list")
        return
    
    def rentFirstAvailableCar(self, expectedReturnDate) -> None:
        first_available_car = self.avRentList.head
        self.avRentList.deleteNode(first_available_car.plate)

        self.rentedList.insertNode(first_available_car.plate, first_available_car.mileage, expectedReturnDate)
        return
    
    def printAllLists(self) -> None:
        print("Available for Rent List:")
        print("---------------------------")
        self.avRentList.printList()
        
        print("Out for Rent List:")
        print("---------------------------")
        self.rentedList.printList()
        
        print("In Repair List:")
        print("---------------------------")
        self.repairList.printList()
        return

