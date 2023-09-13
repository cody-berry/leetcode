class Solution:
    def minimumPossibleSumWithSet(self, n: int, target: int) -> int:
        # define the current sum.
        currentSum = 0
        
        # define the last number. starts at 1.
        lastNumber = 1
        
        # define the invalid numbers set. 
        invalidNumbers = set()
        
        # for n repetitions...
        for i in range(n):
            # while the last number is in the invalid numbers set...
            while lastNumber in invalidNumbers:
                # increment the last number. 
                lastNumber += 1
                
            # add the last number to the list (or to the current sum.)
            currentSum += lastNumber
            
            # add the last number and target minus the last number to 
            # the invalid numbers set.
            invalidNumbers.add(lastNumber)
            invalidNumbers.add(target-lastNumber)
            
        # return the current sum.
        return currentSum


    def minimumPossibleSum(self, n: int, target: int) -> int:
        # all numbers until target/2 are valid. then, all numbers after target are valid.
        # if n=12 and target=12, a valid list would be [1, 2, 3, 4, 5, 6, 12, 13, 14, 15, 16, 17, 18]
        # if n=3 and target=12, a valid list would be [1, 2, 3]
        # generally, a valid list would be [1, 2, 3, ..., target//2 - 1, target//2, target, target+1, ..., target+n-target//2-1]
        
        # if n is less than target//2, then return the triangular number of n
        if n <= target//2:
            return int(((n+1)*n)/2)
        else:
            # otherwise, return the sum of:
                # the triangular number of target//2 = sum(1, 2, 3, ..., target//2). if target = 12, it's sum(1,2,3,4,5,6)
                # the triangular number of n-target//2-1 = sum(1, 2, 3, ..., n-target//2-1). if target = 12 and n = 12, it's sum(1,2,3,4,5)
                # (n - target//2 + 1)*target. if target = 12 and n = 12, it's (12-6+1)*12 = 7*12 = 84.
            splittingPoint = target//2
            return (
                splittingPoint*(splittingPoint+1)//2+\
                (n-splittingPoint)*(n-splittingPoint-1)//2+\
                (n-splittingPoint)*target)%(10**9 + 7)
        
