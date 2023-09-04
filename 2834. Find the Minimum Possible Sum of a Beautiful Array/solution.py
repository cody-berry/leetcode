class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
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
