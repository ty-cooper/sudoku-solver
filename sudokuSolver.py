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

for row in range(0,3):
    print(unsolvedPuzzle[row][2])
    

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
    
    while not solved:
        possibleNumbers= []
        temp = []
        
        # Go cell by cell,
            # check row against finishedRow, append differences to possibleNumbers
            # check column against finishedRow, append to temp 
                # only store overlapped numbers (temp and possibleNumbers) in possibleNumbers
                # clear temp
            # check box against finishedRow, append to temp
                # only store overlapped numbers (temp and possibleNumbers) in possibleNumbers
                # clear temp
                
            # if len(possibleNumbers) == 1:
                # change the value from 'X' to the number in possibleNumbers
            # else
                # continue
                
        # We need a way to see if the while loop has looped each cell without encountering an 'X'
            # if it has (done the above)
            # solved = True
            # return solvedPuzzle 
    
        pass
    
