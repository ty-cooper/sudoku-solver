from array import *

unsolvedPuzzle = [
    [["X", "X", "X"], ["X", 6, 2], ["X", 8, 3]],
    [[6, "X", "X"], [8, "X", 9], ["X", "X", "X"]],
    [["X", 1, "X"], ["X", "X", "X"], [9, "X" ,"X"]],
    [[8, "X", "X"], ["X", 2, "X"], ["X", "X", "X"]],
    [[3, 5, "X"], ["X", "X", "X"], [8, "X", 4]],
    [["X", 6, "X"], [5, "X", "X"], ["X", 9, 1]],
    [[5, "X", 6], [4, "X", 8], [3, 1, 7]],
    [[1, "X", 4], ["X", 3, "X"], ["X", "X", "X"]],
    [[7, "X", 9], [2, 1, 5], [6, "X", 8]]
]

# Using cell objects instead.

# unsolvedPuzzle = [
#     [[C1, C2, C3], [C4, C5, C6], [C7, C8, C9]],
#     [[C10, C11, C12], [C13, C14, C15], [C16, C17, C18]],
#     [[C19, C20, C21], [C22, C23, C24], [C25, C26, C27]],
#     [[C28, C29, C30], [C31, C32, C33], [C34, C35, C36]],
#     [[C37, C38, C39], [C40, C41, C42], [C43, C44, C45]],
#     [[C46, C47, C48], [C49, C50, C51], [C52, C53, C54]],
#     [[C55, C56, C57], [C58, C59, C60], [C61, C62, C63]],
#     [[C64, C65, C66], [C67, C68, C69], [C70, C71, C72]],
#     [[C73, C74, C75], [C76, C77, C78], [C79, C80, C81]]
# ]

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
                    
                    if Xcounter == 82:
                        solved = True
                        return solved

                    else:
                        continue
    
    while solved != True:
        # Go cell by cell,
        solved = iterateCell()             
    
solvePuzzle(unsolvedPuzzle)
