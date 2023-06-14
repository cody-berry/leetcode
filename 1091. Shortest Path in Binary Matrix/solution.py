class Solution:
    # Given a grid, returns the shortest clear path from the 
    # top-left corner to the bottom-right corner. A clear path is one 
    # that traverses only 0s and can go diagonally. If there is none,
    # returns -1.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Uses a BFS traversal to get the shortest path from the
        # top-left to the bottom-right so needs a queue. Entries are
        # in the form of [row, col].

        # Define a version of the grid but for the length of the 
        # shortest clear path from the top-left corner to the grid. 
        # Note that entries that haven't been visited are -1. 

        # Set the first of that grid to 1.

        # Define the round number.

        # while there are still entries in the queue...

            # set the rowIndex and colIndex appropriately.

            # if rowIndex and colIndex are at the end, we return the round num.

            # iterate through every possible direction.

                # as long as the element is not 0...

                    # we append the element.

        # -1 means we didn't find anything.
        return -1


