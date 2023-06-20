class Solution:
    # Given a grid containing 0s and 1s, return the shortest clear path 
    # from the top-left corner to the bottom-right corner. A clear path 
    # is one that traverses only 0s and can go to cells that share an 
    # edge or corner. If there is no clear path, return -1.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # There is no clear path if the top-left or bottom-right corner
        # is a 1, as either something is obstructing the start or the 
        # end.
        
        # Uses a queue for a BFS traversal to get the shortest path 
        # from the top-left to the bottom-right so needs a queue. 
        # Each entry is a tuple containing (row, col).

        # Define a visited list containing the rows and cols we've 
        # visited. Uses the same entries that the BFS traversal uses.

        # Define the length of the path.

        # while there are still entries in the queue...

            # get the length of the queue so that we know what parts
            # of the queue are in this iteration.

            # while we're looking at the queue elements from last 
            # round...
            
                # set the rowIndex and colIndex based on the next
                # element of the queue.
    
                # if rowIndex and colIndex are at the end, we've found
                # a clear path from the top-left to the bottom-right.

                # iterate through every possible direction.

                    # as long as the element is 0...

                        # we append the element to the queue.

                        # we append the element to the visited.

        # -1 means we didn't find a clear path.
        return -1


