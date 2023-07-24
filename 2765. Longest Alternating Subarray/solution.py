class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        # define the length of the longest subarray starting at 1
        longestSubarrayLen = 1
        
        # define the current subarray length starting at 1
        currentSubarrayLength = 1
        
        # define the previous number starting at the first number
        previousNum = nums[0]
        
        # for each number that's not the first...
        for i in range(1, len(nums)):
            num = nums[i]
            # the subarray is supposed to look like [3,4,3,4,3,...], 
            # so s[i+1] - s[i] = (-1)^(i+1). 
            if num - previousNum == (-1)**(currentSubarrayLength + 1):
                # if it meets the requirements, make the previous
                # number this number and increment the current
                # subarray length.
                previousNum = num
                currentSubarrayLength += 1
            
            # otherwise...
            else:
                # save the subarray length if needed.
                if currentSubarrayLength > longestSubarrayLen:
                    longestSubarrayLen = currentSubarrayLength
                
                # if the previous number + 1 is this number, make
                # the current subarray length 2 and the previous num
                # this num.
                if previousNum + 1 == num:
                    currentSubarrayLength = 2
                
                # otherwise, make the current subarray length 1 and
                # make the previous num this num.
                if previousNum + 1 != num:
                    currentSubarrayLength = 1
                
                previousNum = num
        
        # if there's no subarray found of more than length 1, return -1.
        # otherwise, return the length of the longest subarray.
        if currentSubarrayLength > longestSubarrayLen:
            longestSubarrayLen = currentSubarrayLength
        if longestSubarrayLen > 1:
            return longestSubarrayLen
        return -1
