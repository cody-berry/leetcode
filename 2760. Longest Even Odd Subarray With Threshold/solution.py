class Solution:
    # You are given a list of numbers, ""nums"", and you're supposed to find the 
    # longest good subarray. A good subarray is a subarray where:
    # a) L is the start and R is the end of the subarray. 
    # b) nums[L] % 2 == 0.
    # c) nums[i] % 2 != nums[i+1] % 2 where L <= i < R - 1
    # d) nums[i] < threshhold where L <= i < R.
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # Define the longest subarray found.
        
        # Define the length of the current subarray, starting at 1 the first 
        # number is less than the threshhold and divisible by 2, and 0 if
        # not.
        
        # Define the previous number considered, starting at the first element of
        # nums.
        
        # For each number that's not the first...
            
            # If the length of the current subarray is 0...
                
                # If this number is divisible by 2 and less than the threshhold, 
                # set the length to 1. Otherwise, it stays at 0.
                
            # Otherwise...
            
                # If this number is different in "even" or "odd" from the 
                # previous number and is less than the threshhold, add 1 to the
                # length of the current subarray.
                
                # Otherwise...
                
                    # Save the length of the previous subarray.
                    
                    # If the number is divisible by 2 and is less than the 
                    # threshhold, set the length to 1. Otherwise, it stays at 0.
        
        # Return the longest subarray found this way.
