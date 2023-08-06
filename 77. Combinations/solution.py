class Solution:
    # Given two integers n and k, this function returns all possible 
    # combinations of k numbers chosen from the range [1, n].
    def combine(self, n: int, k: int) -> List[List[int]]:
        # if k is 0, return an empty list.

        # otherwise, return the result of a helper function.
        return self.rangedCombine(1, n, k)

    # Given three integers start, end, and k, this function returns
    # all possible combinations of k numbers chosen from the range
    # [start, end].
    def rangedCombine(self, start: int, end: int, k: int):
        # if k is 0, return a list containing an empty list.

        # define the result.

        # define the result of a call of rangedCombine with 1 
        # start greater and 1 k less. 

        # for each number from start to end - k inclusive...

            # for each element of this result, append the number
            # at the start.

        # return this result.
