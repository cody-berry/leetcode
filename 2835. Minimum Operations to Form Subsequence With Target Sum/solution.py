class Solution:
    # initialize the number of operations here; it will be used globally
    def __init__(self):
        self.numOperations = 0

    # given an array nums containing powers of 2 and an integer target, 
    # returns the minimum number of operations needed to form a subsequence 
    # that sums up to target. In each operation, choose one of the powers 
    # of 2 that are greater than 1 and add 2 occurences of that power of 2
    # divided by 2 to the end of the array.
    def minOperations(self, nums: List[int], target: int) -> int:
        # a subsequence cannot be formed that sums up to target if
        # the sum of all the nums is less than the target. a subsequence
        # that sums up to target is equal to nums if the sum of all the
        # nums is equal to the target. 
        sumOfNums = sum(nums)
        if target > sumOfNums: return -1
        if target == sumOfNums: return 0
        # Solve the problem for each set bit of target, independently, from 
        # least significant to most significant bit.
        bits = self.findBitsOfNum(target)

        # sort the numbers. it's more convenient that way
        nums = sorted(nums)

        # iterate through each power. modify nums to solve for that power. 
        for bit in bits:
            nums = self.modifyNumsToSolveForBit(nums, bit)

        return self.numOperations

    # given a number, finds all the powers of 2 that are part of num. 
    def findBitsOfNum(self, num):
        bits = []

        # find the maximum bit and power of 2
        currentBit = 0
        currentPow = 1
        while currentPow <= num:
            currentBit += 1
            currentPow *= 2
        if currentBit > 1:
            currentPow //= 2
            currentBit -= 1

        copyOfNum = num

        # find the bits of num by removing powers of 2 repeatedly from 
        # num. 
        while copyOfNum > 0:
            if currentPow <= copyOfNum:
                copyOfNum -= currentPow
                bits.append(currentPow)
            currentPow //= 2
            currentBit -= 1

        bits = sorted(bits)

        return bits

    def modifyNumsToSolveForBit(self, nums, power):
        # the least power that is greater than the power.
        resortNumber = 0 

        # the index of the first occurence of the least power that is greater 
        # than the power.
        indexOfResortNumber = 0

        # the nums that are less than or equal to the power.
        numsPartOfX = [] 

        # the sum of all numbers in nums less than or equal to power.
        X = 0 

        # iterate through nums.
        for num in nums:
            # if it's less than the power, the number is part of X.
            if num < power:
                X += num
                numsPartOfX.append(num)

            # if it's equal to the power, we've already gotten an 
            # element that, alone, sums up to nums. 
            if num == power:
                nums.remove(num)
                return nums
            
            # if the number is greater than the power, this is the
            # first resort number. since nums is sorted, this is the
            # least number. 
            if num > power:
                resortNumber = num
                break

            # track the index we're on.
            indexOfResortNumber += 1

        # sort numsPartOfX. 
        numsPartOfX = sorted(numsPartOfX)

        # repeatedly select the maximum number that is part of X until
        # those numbers sum up to the power. 
        if X >= power:
            sumOfSelectedNums = 0

            # select the numbers
            while sumOfSelectedNums < power:
                # select a num, and only register it if it's valid.
                selectedNum = numsPartOfX.pop()
                if selectedNum <= (power - sumOfSelectedNums):
                    sumOfSelectedNums += selectedNum
                    nums.remove(selectedNum)
                
        # otherwise, break the resort number down in-place. this
        # counts as an operation. then, go back to this function.
        # there has to be a resort number because as a given, we 
        # already know that a solution exists. 
        # note: this is where indexOfResortNumber comes in handy.
        else:
            nums.remove(resortNumber)
            nums.insert(indexOfResortNumber, resortNumber//2)
            nums.insert(indexOfResortNumber, resortNumber//2)
            self.numOperations += 1
            nums = self.modifyNumsToSolveForBit(nums, power)
            
        return nums
