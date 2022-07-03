from array import *
from sudokuCell import Cell

C1 = Cell("C1")
C2 = Cell("C2")
C3 = Cell("C3")
C4 = Cell("C4")
C5 = Cell("C5", 6)
C6 = Cell("C6", 2)
C7 = Cell("C7")
C8 = Cell("C8", 8)
C9 = Cell("C9", 3)

C10 = Cell("C10", 6)
C11 = Cell("C11")
C12 = Cell("C12")
C13 = Cell("C13", 8)
C14 = Cell("C14")
C15 = Cell("C15", 9)
C16 = Cell("C16")
C17 = Cell("C17")
C18 = Cell("C18")

C19 = Cell("C19")
C20 = Cell("C20", 1)
C21 = Cell("C21")
C22 = Cell("C22")
C23 = Cell("C23")
C24 = Cell("C24")
C25 = Cell("C25", 9)
C26 = Cell("C26")
C27 = Cell("C27")

C28 = Cell("C28", 8)
C29 = Cell("C29")
C30 = Cell("C30")
C31 = Cell("C31")
C32 = Cell("C32", 2)
C33 = Cell("C33")
C34 = Cell("C34")
C35 = Cell("C35")
C36 = Cell("C36")

C37 = Cell("C37", 3)
C38 = Cell("C38", 5)
C39 = Cell("C39")
C40 = Cell("C40")
C41 = Cell("C41")
C42 = Cell("C42")
C43 = Cell("C43", 8)
C44 = Cell("C44")
C45 = Cell("C45", 4)

C46 = Cell("C46")
C47 = Cell("C47", 6)
C48 = Cell("C48")
C49 = Cell("C49", 5)
C50 = Cell("C50")
C51 = Cell("C51")
C52 = Cell("C52")
C53 = Cell("C53", 9)
C54 = Cell("C54", 1)

C55 = Cell("C55", 5)
C56 = Cell("C56")
C57 = Cell("C57", 6)
C58 = Cell("C58", 4)
C59 = Cell("C59")
C60 = Cell("C60", 8)
C61 = Cell("C61", 3)
C62 = Cell("C62", 1)
C63 = Cell("C63", 7)

C64 = Cell("C64", 1)
C65 = Cell("C65")
C66 = Cell("C66", 4)
C67 = Cell("C67")
C68 = Cell("C68", 3)
C69 = Cell("C69")
C70 = Cell("C70")
C71 = Cell("C71")
C72 = Cell("C72")

C73 = Cell("C73", 7)
C74 = Cell("C74")
C75 = Cell("C75", 9)
C76 = Cell("C76", 2)
C77 = Cell("C77", 1)
C78 = Cell("C78", 5)
C79 = Cell("C79", 6)
C80 = Cell("C80")
C81 = Cell("C81", 8)


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

def solvePuzzle(puzzle):
    finishedRow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solved = False
    unsolvedPuzzle = puzzle
    
    def checkNakedSingle(row, box, column):
         # This could be refactored into checking the different possible solutions.
        
        """
        While iterating:
        
        if 'X':
            naked_single()
            if naked_single:
                continue
            else:
                hidden_single()
                if hidden_single():
                    continue
                ...
                    ...etc.
        """

        possibleNumbers = []
        rowNums = []
        transfer = []
        
        # check1 row possible, append to list
        for iterateBox in unsolvedPuzzle[row]:
            for number in iterateBox:
                rowNums.append(number)
                
        for cell in rowNums:
            transfer.append(cell.getValue())
                
        missingNums = set(finishedRow).difference(set(transfer))
        for number in missingNums:
            possibleNumbers.append(number)
            
        # check2 column possible, append to list
        for iterateRow in range(0, len(unsolvedPuzzle)):
            number = unsolvedPuzzle[iterateRow][box][column]
            if number.getValue() in possibleNumbers:
                possibleNumbers.remove(number.getValue())
            
        # check3 box possible, append to list
        if row <= 2:
            for iterateRow in range(3):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    if boxNumber.getValue() in possibleNumbers:
                        possibleNumbers.remove(boxNumber.getValue())
                    
        if row >= 3 and row <= 5:
            for iterateRow in range(3, 6):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    if boxNumber.getValue() in possibleNumbers:
                        possibleNumbers.remove(boxNumber.getValue())
                        
        if row >= 6:
            for iterateRow in range(6, 9):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    if boxNumber.getValue() in possibleNumbers:
                        possibleNumbers.remove(boxNumber.getValue())
                        
        return possibleNumbers
    
    def checkHiddenSingle(row, box, column):
        # Same as above, but instead of just using values- we fetch objects from values
        # and compare their .getPossibleNumbers attribute.
        
        possibleNumbers = []
        rowNums = []
        columnNums = []
        boxNums = []
        
        # check1 row possible, append to list
        for iterateBox in unsolvedPuzzle[row]:
            for number in iterateBox:
                rowNums.append(number)
            
        # check2 column possible, append to list
        for iterateRow in range(0, len(unsolvedPuzzle)):
            number = unsolvedPuzzle[iterateRow][box][column]
            columnNums.append(number)
            
        # check3 box possible, append to list
        if row <= 2:
            for iterateRow in range(3):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    boxNums.append(boxNumber)
                    
        if row >= 3 and row <= 5:
            for iterateRow in range(3, 6):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    boxNums.append(boxNumber)
                        
        if row >= 6:
            for iterateRow in range(6, 9):
                for boxNumber in unsolvedPuzzle[iterateRow][box]:
                    boxNums.append(boxNumber)
                    
        ###                    
        
        [possibleNumbers.append(f"Box: {cell}") for cell in boxNums]
        [possibleNumbers.append(f"Row: {cell}") for cell in rowNums]
        [possibleNumbers.append(f"Column: {cell}") for cell in columnNums]
        
        
            
        return possibleNumbers
    
    # def checkHiddenSingle(row, box, column):
    #     possibleNums = []
    #     rowNums = []
    #     transfer = []
        
    #     columnNums = []
    #     boxNums = []
        
    #     # Check row
    #     for iterateBox in unsolvedPuzzle[row]:
    #         for number in iterateBox:
    #             rowNums.append(number)
                
    #     for cell in rowNums:
    #         transfer.append(cell.getValue())
            
    #     missingNums = set(finishedRow).difference(set(transfer))
    #     for number in missingNums:
    #         possibleNums.append(number)
            
    #     for value in transfer:
        
        # compile a list of all the possible numbers of every cell around the current
        # save these because we need to figure out how to save possibleNums to the cell object
        # We will essentially be running possibleNumbers (above) on every iteration, saving the list
        # Save the list of possible numbers to the possible number variable

    
    def iterateCell():
        Xcounter = 0
        
        for row in range(len(unsolvedPuzzle)):
            for box in range(3):
                for column in range(3):
                    print('\n**********')
                    print('**********')
                    currentCell = unsolvedPuzzle[row][box][column]
                    print(f"Position: {currentCell.getName()}")
                
                    if currentCell.getValue() == 'X':
                        Xcounter = 0
                        solution = checkNakedSingle(row, box, column)
                        print(solution)
                        if len(solution) == 1:
                            currentCell.setValue(solution.pop())
                            print(f"X is now {currentCell.getValue()}")
                        elif len(solution) >= 2:
                            # this is how we can now check for hidden singles
                            currentCell.setPossibleNumbers(solution)
                            
                            solution = checkHiddenSingle(row, box, column)
                            print(solution)
                                
                        elif len(solution) == 0:
                            print("ERROR: Unsolvable")
                            
                    else:
                        Xcounter += 1
                                        
                    
                    print(currentCell)
                    print(currentCell.getValue())
                    print(f"Row: {row}")
                    print(f"Column: {column}")
                    print(f"Box: {box}")
                    print(f"Xcounter: {Xcounter}")
                    print('**********')
                    print('**********\n')
                    
                    if Xcounter >= 82:
                        solved = True
                        print("Solved.")
                        return solved
                    
                    goOn = input("Next? ")
                    if goOn == 'y':
                        solved = True
                        return solved
                    else:
                        continue
    
    while solved != True:
        solved = iterateCell()             
    
solvePuzzle(unsolvedPuzzle)

