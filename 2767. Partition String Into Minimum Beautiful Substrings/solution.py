class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # define the number of blocks that contain 0, 1, 2, 3, or 4 black cells. 
        
        # create a new grid with a width of m-1 and a height of n-1. in doing so, add to the 
        # number of blocks that contain 0 cells.
        
        # for each black cell...

            # extract the x and y coordinates of the cell. 
            
            # iterate through each cell that is either 1 left, 1 up, 1 left and 1 up, or on
            # this cell. add 1 to it, and depending on the result, add/subtract from the
            # number of blocks that contain a certain number of black cells.
        
        # return [zeroBlackCellsInBlock, oneBlackCellInBlock, ...fourBlackCellsInBlock]
        return [0, 0, 0, 0, 0]
