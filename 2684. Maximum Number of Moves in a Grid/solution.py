class Solution:
    # Given a grid, it determines the maximum moves possible in a grid. Starting from any cell in
    # the first column, it always goes right. It can either stay in the same column, go up, or go 
    # down. A move like this always has to have the resulting number be greater and not equal to
    # the current number. 
    def maxMoves(self, grid: List[List[int]]) -> int:
        ### VARIABLE INITIALIZATION
        
        # what is the maximum number of moves
        maxMoves = 0
        
        # column length
        colLen = len(grid)
        
        # row length
        rowLen = len(grid[0])
        
        # the stack starts with the entries in the first column
        stack = []
        for i in range(0, colLen):
            stack.append([i, 0, 0])
            
        # the visited starts with nothing. the current entries of
        # the stack will never be visited again
        visited = set()
        
        ### DFS IMPLEMENTATION
        while stack:
            # Pop from the stack and get the row, col, num, and moves. 
            entry = stack.pop()

            # colIndex is the index INSIDE the column
            colIndex = entry[0]

            # rowIndex is the index INSIDE the row
            rowIndex = entry[1]

            num = grid[colIndex][rowIndex]
            moves = entry[2]
            
            # Iterate through the element to the right, the element diagonally to the top-right, and the 
            # element diagonally to the bottom-right.
            if (rowIndex+1 < rowLen):
                appendedToStack = False
                for newEntry in (
                    [[colIndex-1, rowIndex+1], 
                     [colIndex, rowIndex+1], 
                     [colIndex+1, rowIndex+1]]
                    ):
                    if (newEntry[0] >= 0) and (newEntry[0] < colLen):
                        # If that pair in the grid is greater (exclusive)
                        # than this number and it hasn't been explored 
                        # before, we add it to the stack.
                        if grid[newEntry[0]][newEntry[1]] > num:
                            appendedToStack = True
                            stack.append([newEntry[0], newEntry[1], moves+1])
            else:
                # If col+1 doesn't exist, then return the length of 
                # the grid minus 1. 
                return rowLen - 1
            
            # If something was appended to the grid and the number of
            # moves so far is greater than the max moves available, 
            # make the max moves the number of moves. 
            if appendedToStack and moves == maxMoves:
                maxMoves = moves + 1
            
        return maxMoves
        
