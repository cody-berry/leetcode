class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # iterate through the array, checking if it's a rotated sorted aray
        lastNumber = nums[0]
        smallestNumberIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > lastNumber: 
                if smallestNumberIndex > 0:
                    if nums[i] > nums[0]:
                        return -1
            else:
                if smallestNumberIndex > 0:
                    return -1
                smallestNumberIndex = i
            lastNumber = nums[i]
        return (len(nums) - smallestNumberIndex) if smallestNumberIndex > 0 else 0
                    
                
