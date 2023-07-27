class Solution:
    # Given a list of marbles (nums), this function returns a list of the occupied positions of the
    # marbles. Each element in nums represents a position, and you are supposed to move each marble
    # in that position 
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        # convert nums to a set.
        setNums = set(nums)
        
        # for each element in moveFrom...
        for i in range(len(moveFrom)):
            # there is garunteed to be an instance of moveFrom[i] in each iteration and only one.
            setNums.remove(moveFrom[i])
            setNums.add(moveTo[i])
        
        # return sorted nums as a list.
        return sorted(list(setNums))
        
                
