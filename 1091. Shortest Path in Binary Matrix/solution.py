class Solution:
    # Given a grid containing 0s and 1s, return the shortest clear path 
    # from the top-left corner to the bottom-right corner. A clear path 
    # is one that traverses only 0s and can go to cells that share an 
    # edge or corner. If there is no clear path, return -1.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # There is no clear path if the top-left or bottom-right corner
        # is a 1, as either something is obstructing the start or the 
        # end.
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # Uses a queue for a BFS traversal to get the shortest path 
        # from the top-left to the bottom-right so needs a queue. 
        # Each entry is a tuple containing (colIndex, rowIndex).
        queue = [(0, 0)]

        # Define a visited list containing the rows and cols we've 
        # visited. Uses the same entries that the BFS traversal uses.
        visited = set()
        visited.add((0, 0))

        # Define the length of the path.
        roundNum = 1

        # while there are still entries in the queue...
        while (queue):
            # get the length of the queue so that we know what parts
            # of the queue are in this iteration.
            lenQueue = len(queue)

            # while we're looking at the queue elements from last 
            # round...
            for i in range(lenQueue):
                # set the rowIndex and colIndex based on the next
                # element of the queue. the structure makes it so
                # that the first added, the one at index 0, is the
                # first out, which means that the one at index 0 is
                # the first out.
                currentElement = queue.pop(0)

                # colIndex is the index inside the column and 
                # rowIndex is the index inside the row.
                colIndex = currentElement[0]
                rowIndex = currentElement[1]
    
                # if rowIndex and colIndex are at the end, we've found
                # a clear path from the top-left to the bottom-right.
                # note that the the grid is a square grid so the length
                # on either side is the same.
                if colIndex == len(grid) - 1 and rowIndex == len(grid) - 1:
                    return roundNum

                # iterate through every possible direction.
                for direction in [
                    [0, 1], # right
                    [1, 1], # up and right
                    [1, 0], # up
                    [1, -1], # up and left
                    [0, -1], # left
                    [-1, -1], # down and left
                    [-1, 0], # down
                    [-1, 1], # down and right
                ]:
                    
                    # check for borders
                    if ((0 <= colIndex + direction[0]) and (colIndex + direction[0] < len(grid)) and
                       (0 <= rowIndex + direction[1]) and (rowIndex + direction[1] < len(grid))):
                        # as long as the element is 0 and we haven't visited it...
                        if grid[colIndex + direction[0]][rowIndex + direction[1]] == 0 and not (colIndex + direction[0], rowIndex + direction[1]) in visited:
                            # we append the element to the queue.
                            queue.append((colIndex + direction[0], rowIndex + direction[1]))

                            # we append the element to the visited.
                            visited.add((colIndex + direction[0], rowIndex + direction[1]))
            
            roundNum += 1

        # -1 means we didn't find a clear path.
        return -1
