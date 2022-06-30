
class Cell:
    """
    Basic Cell Object in a Sudoku Puzzle.
    """
    
    def __init__(self, name, val='X'):
        self.name = name
        self.value = val
        
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
        
    def getPossibleNumbers(self):
        possibleNumbers = []
        return possibleNumbers
    
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



    
        