class Solution:
    # Given an array of nums, return all possible permutations 
    # of that array.
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if nums is length 1, return [[nums[0]]]

        # define the result.

        # for each number in nums...

            # permute nums again, but this time without the
            # number we're starting with.

            # for each element in it, append the starting num
            # to it, then append it to result.

        # return the result.
