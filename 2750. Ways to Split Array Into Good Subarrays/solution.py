class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # Iterate until the first 1. 
        
        # Keep count of the number of 0s.
        
        # For each number...
        
            # If it's a 0, add to the count of 0s.
            
            # If it's a 1, then multiply the result by the num of 0s plus 1. Then reset the count of 0s.
