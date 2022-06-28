from array import *
from turtle import pos

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
        for iterateRow in range(3):
            for number in unsolvedPuzzle[iterateRow][box]:
                if number in possibleNumbers:
                    possibleNumbers.remove(number)
                
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
                    
                    if Xcounter == 82:
                        solved = True
                        return solved
            
    
    while solved != True:
        # Go cell by cell,
        solved = iterateCell()             
    
solvePuzzle(unsolvedPuzzle)
