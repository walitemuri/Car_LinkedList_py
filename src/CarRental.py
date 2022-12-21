from Lists.AvailableForRent import AvailableRentList
from Lists.Rented import RentedList
from Lists.InRepair import RepairList
from Interface.Interface import Interface

class CarRental:
    def __init__(self) -> None:
        self.avRentList = AvailableRentList()
        self.rentedList = RentedList()
        self.repairList = RepairList()
        self.interface = Interface()
    
    def addNewCarToAvRentList(self, carPlate, mileage):
        self.avRentList.insertNode(carPlate, mileage)
        return
    
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
        print("\nAvailable for Rent List:\n")
        self.avRentList.printList()
        print("---------------------------")
        
        print("Out for Rent List:\n")
        self.rentedList.printList()
        print("---------------------------")
        
        print("In Repair List:\n")
        self.repairList.printList()
        print("---------------------------")
        return

def main ():
    CarRentalResolver = CarRental()
    user_input = -1
    while user_input != 7:
        user_input = CarRentalResolver.interface.getInteger(CarRentalResolver.interface.printMenu())
        
        

        if user_input == 1:
            plate_input = CarRentalResolver.interface.getPlateInput()
            miles_input = CarRentalResolver.interface.getMileInput()
            CarRentalResolver.addNewCarToAvRentList(plate_input, miles_input)
        elif user_input == 2:
            plate_input = CarRentalResolver.interface.getPlateInput()
            miles_input = CarRentalResolver.interface.getMileInput()
            CarRentalResolver.addReturnedCarToAvailableList(plate_input, miles_input)
        elif user_input == 3:
            plate_input = CarRentalResolver.interface.getPlateInput()
            miles_input = CarRentalResolver.interface.getMileInput()
            CarRentalResolver.addReturnedCarToRepairList(plate_input, miles_input)
        elif user_input == 4:
            plate_input = CarRentalResolver.interface.getPlateInput()
            CarRentalResolver.transferCarFromRepairToAvRentList(plate_input)
        elif user_input == 5:
            expectedReturn_input = CarRentalResolver.interface.getExpectedReturnDate()
            CarRentalResolver.rentFirstAvailableCar(expectedReturn_input)
        elif user_input == 6:
            CarRentalResolver.printAllLists()
        elif user_input == 7:
            pass
        else:
            pass
main()