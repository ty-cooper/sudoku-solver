
class Cell:
    """
    Basic Cell Object in a Sudoku Puzzle.
    """
    
    def __init__(self, name, val='X'):
        self.name = name
        self.value = val
        self.possibleNumbers = []
        
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def findCell(self):
        # If i plug in a name, I want to search cells and pull the relateed one.
        # this would be higher than this
        pass
    
    def setValue(self, val):
        self.value = val
        
    def getPossibleNumbers(self):
        return self.possibleNumbers
    
    def setPossibleNumbers(self, possibleNumbers):
        self.possibleNumbers = possibleNumbers
    
    def getContext(self):
        self.rowNumbers = []
        self.columnNumbers = []
        self.boxNumbers = []
        
        context = {
            "row": self.rowNumbers,
            "column": self.columnNumbers,
            "box": self.boxNumbers
        }
        return context
    
C1 = Cell("C1")

print(C1.getName())
print(C1.getValue())



    
        