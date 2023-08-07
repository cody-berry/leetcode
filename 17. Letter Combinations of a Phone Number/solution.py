class Solution:
    # Given an array of nums, return all possible permutations 
    # of that array.
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if nums is length 1, return [[nums[0]]]
        if len(nums) == 1:
            return [[nums[0]]]

        # define the result.
        result = []

        # for each number in nums...
        for i in range(len(nums)):
            # permute nums again, but this time without the
            # number we're starting with.
            newNums = nums.copy()
            num = newNums.pop(i)
            previousResult = self.permute(newNums)

            # for each element in it, append the starting num
            # to it, then append it to result.
            for permutation in previousResult:
                permutation.append(nums[i])
                result.append(permutation)

        # return the result.
        return result
