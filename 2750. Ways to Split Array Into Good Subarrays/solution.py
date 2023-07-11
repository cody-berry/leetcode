class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # Iterate until the first 1. 
        i = 0
        try:
            while nums[i] == 0:
                i += 1
        except:
            return 0
        
        # Keep count of the number of 0s.
        numZeroes = 0
        
        # For each number...
        result = 1
        for j in range(i+1, len(nums)):
            # If it's a 0, add to the count of 0s.
            if nums[j] == 0:
                numZeroes += 1
            
            # If it's a 1, then multiply the result by the num of 0s plus 1. Then reset the count of 0s.
            else:
                result *= numZeroes + 1
                numZeroes = 0
                
        return result % (10**9 + 7)
