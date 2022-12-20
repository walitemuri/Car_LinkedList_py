class Interface:
    def __init__(self) -> None:
        pass

    def printMenu(self) -> None:
        print("1 - Add a new car to the available for rent list")
        print("2 - Add a returned car to the available-for-rent list")
        print("3 - Add a returned car to the repair list")
        print("4 - Transfer a car from the repair list to the available-for-rent list")
        print("5 - Rent the first available car")
        print("6 - Print all the lists")
        print("7 - Quit")
        return

    def getInteger(self) -> int:
        return int(input())
    
    def getStr(self) -> str:
        return input()

