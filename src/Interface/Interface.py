from datetime import datetime
class Interface:
    """
    Class Template for Menu Interface with user
    ...

    Attributes
    ----------
    None
    """
    def __init__(self) -> None:
        pass

    def printMenu(self) -> str:
        print("1 - Add a new car to the available for rent list")
        print("2 - Add a returned car to the available-for-rent list")
        print("3 - Add a returned car to the repair list")
        print("4 - Transfer a car from the repair list to the available-for-rent list")
        print("5 - Rent the first available car")
        print("6 - Print all the lists")
        print("7 - Quit")
        return ""

    def getInteger(self, msg) -> int:
        try:
            user_input = int(input(msg))
            return user_input
        except ValueError:
            print("Please enter a valid number")
            return
    
    def getStr(self, msg) -> str:
        return input(msg)

    def getPlateInput(self) -> str:
        user_input = input("Enter Plate: ")
        return user_input

    def getMileInput(self):
        user_input = self.getInteger("Enter Miles: ")
        return user_input

    def getExpectedReturnDate(self) -> str:
        user_input = self.getStr("Enter Expected Return(YYYY-MM-DD): ")

        try:
            datetime.strptime(user_input, '%Y-%m-%d')
            return user_input
        except ValueError:
            raise ValueError("Incorrect Date Time Format.")
            
