class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        # define the length of the longest subarray starting at 1
        
        # define the current subarray length starting at 1
        
        # define the previous number starting at the first number
        
        # for each number that's not the first...
        
            # the subarray is supposed to look like [3,4,3,4,3,...], 
            # so s[i+1] - s[i] = (-1)^(i+1). 
            
                # if it meets the requirements, make the previous
                # number this number and increment the current
                # subarray length.
            
            # otherwise...
            
                # save the subarray length if needed.
                
                # if the previous number + 1 is this number, make
                # the current subarray length 2 and the previous num
                # this num.
                
                # otherwise, make the current subarray length 1 and
                # make the previous num this num.
        
        # if there's no subarray found of more than length 1, return -1.
        # otherwise, return the length of the longest subarray.
        return -1
