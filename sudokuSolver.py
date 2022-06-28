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
    
    def calculatePossibleNumbers():
        possibleNumbers = []
            # check possibleNumbers for:
                
                # check1 row possible, append to list
    
                # check2 column possible, append to list
    
                # check3 box possible, append to list
    
                # decide: 
                    # if len(possibleNumbers) == 1:
                        # currentCell = possibleNumbers[0]
                        # continue
        return possibleNumbers
    
    def iterateCell():
        
        for row in range(len(unsolvedPuzzle)):
            for box in range(3):
                for column in range(3):
                    currentCell = unsolvedPuzzle[row][box][column]
                    
                    if currentCell == 'X':
                        Xcounter = 0
                        possibleNumbers = calculatePossibleNumbers()
                        if len(possibleNumbers) == 1:
                            currentCell = possibleNumbers.pop()
                    
                    Xcounter += 1
                                        
                    print(currentCell)
                    print(f"Row: {row}")
                    print(f"Column: {column}")
                    print(f"Box: {box}")
                    
                    goNext = input("Next? ")
                    
                    if goNext == 'y':
                        continue
                    elif Xcounter == 82:
                        solved = True
                        return solved
                    else:
                        solved = True
                        return solved
            
        solved = True
        return solved
    
    while solved != True:
        possibleNumbers= []
        temp = []
        
        # Go cell by cell,
        solved = iterateCell()             
    
solvePuzzle(unsolvedPuzzle)
