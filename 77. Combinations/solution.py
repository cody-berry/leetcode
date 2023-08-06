class Solution:
    # Given two integers n and k, this function returns all possible 
    # combinations of k numbers chosen from the range [1, n].
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return the result of a helper function.
        return self.rangedCombine(1, n, k)

    # Given three integers start, end, and k, this function returns
    # all possible combinations of k numbers chosen from the range
    # [start, end].
    def rangedCombine(self, start: int, end: int, k: int):
        # if k is 0, return a list containing an empty list.
        if k == 0:
            return [[]]

        # define the result.
        result = []

        # for each number from start to end - k + 1 inclusive...
        for i in range(start, end - k + 2):
            # define the result of a call of rangedCombine with 1 
            # start greater than i and 1 k less. 
            previousResult = self.rangedCombine(i + 1, end, k - 1)

            # for each element of this result, append the number
            # at the start.
            for combination in previousResult:
                combination.append(i)
                result.append(combination)

        # return this result.
        return result
