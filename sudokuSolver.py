from array import *
from sudokuCell import Cell

# Initializing the cells
# theres got to be a better way to do this

C1 = Cell("C1")
C2 = Cell("C2")
C3 = Cell("C3")
C4 = Cell("C4")
C5 = Cell(6, "C5")
C6 = Cell(2, "C6")
C7 = Cell("C7")
C8 = Cell(8, "C8")
C9 = Cell(3, "C9")

C10 = Cell(6, "C10")
C11 = Cell("C11")
C12 = Cell("C12")
C13 = Cell(8, "C13")
C14 = Cell("C14")
C15 = Cell(9, "C15")
C16 = Cell("C16")
C17 = Cell("C17")
C18 = Cell("C18")

C19 = Cell("C19")
C20 = Cell(1, "C20")
C21 = Cell("C21")
C22 = Cell("C22")
C23 = Cell("C23")
C24 = Cell("C24")
C25 = Cell(9, "C25")
C26 = Cell("C26")
C27 = Cell("C27")

C28 = Cell(8, "C28")
C29 = Cell("C29")
C30 = Cell("C30")
C31 = Cell("C31")
C32 = Cell(2, "C32")
C33 = Cell("C33")
C34 = Cell("C34")
C35 = Cell("C35")
C36 = Cell("C36")

C37 = Cell(3, "C37")
C38 = Cell(5, "C38")
C39 = Cell("C39")
C40 = Cell("C40")
C41 = Cell("C41")
C42 = Cell("C42")
C43 = Cell(8, "C43")
C44 = Cell("C44")
C45 = Cell(4, "C45")

C46 = Cell("C46")
C47 = Cell(6, "C47")
C48 = Cell("C48")
C49 = Cell(5, "C49")
C50 = Cell("C50")
C51 = Cell("C51")
C52 = Cell("C52")
C53 = Cell(9, "C53")
C54 = Cell(1, "C54")

C55 = Cell(5, "C55")
C56 = Cell("C56")
C57 = Cell(6, "C57")
C58 = Cell(4, "C58")
C59 = Cell("C59")
C60 = Cell(8, "C60")
C61 = Cell(3, "C61")
C62 = Cell(1, "C62")
C63 = Cell(7, "C63")

C64 = Cell(1, "C64")
C65 = Cell("C65")
C66 = Cell(4, "C66")
C67 = Cell("C67")
C68 = Cell(3, "C68")
C69 = Cell("C69")
C70 = Cell("C70")
C71 = Cell("C71")
C72 = Cell("C72")

C73 = Cell(7, "C73")
C74 = Cell("C74")
C75 = Cell(9, "C75")
C76 = Cell(2, "C76")
C77 = Cell(1, "C77")
C78 = Cell(5, "C78")
C79 = Cell(6, "C79")
C80 = Cell("C80")
C81 = Cell(8, "C81")


# unsolvedPuzzle = [
#     [["X", "X", "X"], ["X", 6, 2], ["X", 8, 3]],
#     [[6, "X", "X"], [8, "X", 9], ["X", "X", "X"]],
#     [["X", 1, "X"], ["X", "X", "X"], [9, "X" ,"X"]],
#     [[8, "X", "X"], ["X", 2, "X"], ["X", "X", "X"]],
#     [[3, 5, "X"], ["X", "X", "X"], [8, "X", 4]],
#     [["X", 6, "X"], [5, "X", "X"], ["X", 9, 1]],
#     [[5, "X", 6], [4, "X", 8], [3, 1, 7]],
#     [[1, "X", 4], ["X", 3, "X"], ["X", "X", "X"]],
#     [[7, "X", 9], [2, 1, 5], [6, "X", 8]]
# ]

# Using cell objects instead.

unsolvedPuzzle = [
    [[C1, C2, C3], [C4, C5, C6], [C7, C8, C9]],
    [[C10, C11, C12], [C13, C14, C15], [C16, C17, C18]],
    [[C19, C20, C21], [C22, C23, C24], [C25, C26, C27]],
    [[C28, C29, C30], [C31, C32, C33], [C34, C35, C36]],
    [[C37, C38, C39], [C40, C41, C42], [C43, C44, C45]],
    [[C46, C47, C48], [C49, C50, C51], [C52, C53, C54]],
    [[C55, C56, C57], [C58, C59, C60], [C61, C62, C63]],
    [[C64, C65, C66], [C67, C68, C69], [C70, C71, C72]],
    [[C73, C74, C75], [C76, C77, C78], [C79, C80, C81]]
]

# Row: unsolvedPuzzle[n]

# Column: for row in range(0, len(unsolvedPuzzle)):
#    return unsolvedPuzzle[row][box][column]

# Box: for row in range(boxHeight):
#    return unsolvedPuzzle[row][box]

# for row in unsolvedPuzzle:
#     for solutionNumber in finishedRow:
#         if solutionNumber not in row:
#             print(solutionNumber)


# print(unsolvedPuzzle[0][1][2])
    

"""
1. How could we model sudoku in python?
Using a 2D array.
9x9

2. Select a puzzle and model it in python

3. Figure out how to check the row, column, and box for possible numbers

4. Use the tests to check every row, column, and box for possible numbers
As they check, remove any numbers not shared between the three checks

5. Each iteration, replace X only when there is only one possible solution

6. Iterate until X is not in unsolvedPuzzle

7. Save it as an array object as solvedPuzzle
"""

def solvePuzzle(puzzle):
    finishedRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solved = False
    unsolvedPuzzle = puzzle
    
    def calculatePossibleNumbers(row, box, column):
        possibleNumbers = []
        rowNums = []
                
        # check1 row possible, append to list
        for iterateBox in unsolvedPuzzle[row]:
            for number in iterateBox:
                rowNums.append(number)
                
        missingNums = set(finishedRow).difference(set(rowNums))
        for number in missingNums:
            possibleNumbers.append(number)
            
        # check2 column possible, append to list
        for iterateRow in range(0, len(unsolvedPuzzle)):
            number = unsolvedPuzzle[iterateRow][box][column]
            if number in possibleNumbers:
                possibleNumbers.remove(number)
            
        # check3 box possible, append to list
        if row <= 2:
            for iterateRow in range(3):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    if boxNumber in possibleNumbers:
                        possibleNumbers.remove(boxNumber)
                    
        if row >= 3 and row <= 5:
            for iterateRow in range(3, 6):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    if boxNumber in possibleNumbers:
                        possibleNumbers.remove(boxNumber)
                        
        if row >= 6:
            for iterateRow in range(6, 9):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    if boxNumber in possibleNumbers:
                        possibleNumbers.remove(boxNumber)
                
        # Currently, we have every 'X' appending all possible solutions to each cell.
        # Last step is to eliminate overlap.
        # What determines whats allowed to stay in possibleNumbers?
            
        return possibleNumbers
    
    def iterateCell():
        Xcounter = 0
        position = 0
        
        for row in range(len(unsolvedPuzzle)):
            for box in range(3):
                for column in range(3):
                    position += 1
                    print('\n**********')
                    print('**********')
                    print(f"Position: {position}")
                    currentCell = unsolvedPuzzle[row][box][column]
                    
                    if currentCell == 'X':
                        Xcounter = 0
                        possibleNumbers = calculatePossibleNumbers(row, box, column)
                        print(possibleNumbers)
                        if len(possibleNumbers) == 1:
                            unsolvedPuzzle[row][box][column] = possibleNumbers.pop()
                            print(f"X is now {unsolvedPuzzle[row][box][column]}")
                        elif len(possibleNumbers) == 0:
                            
                            print("ERROR: Unsolvable")
                            
                    else:
                        Xcounter += 1
                                        
                    
                    print(currentCell)
                    print(f"Row: {row}")
                    print(f"Column: {column}")
                    print(f"Box: {box}")
                    print(f"Xcounter: {Xcounter}")
                    print('**********')
                    print('**********\n')
                    
                    goOn = input("Next? ")
                    if goOn == 'y':
                        solved = True
                        return solved
                    
                    elif Xcounter >= 82:
                        solved = True
                        return solved

                    else:
                        continue
    
    while solved != True:
        # Go cell by cell,
        solved = iterateCell()             
    
solvePuzzle(unsolvedPuzzle)
