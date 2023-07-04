class Solution:
    # Given a list of nums, this function returns the number of beautiful pairs. 
    # A pair of numbers is called "beautiful" if the greatest common divisor of 
    # the first digit of the first number and the last digit of the second
    # number have a greatest common divisor of 1, which is exactly what the
    # second function handles.
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # define the number of beautiful pairs.
        numBeautifulPairs = 0

        # define a list of tuples containing the first and last digits of the 
		# respective number.
        numTuples = []
        for num in nums:
            # make appending elements by transforming the number into a string
            numString = str(num)
            numTuples.append((int(numString[0]), int(numString[-1])))
        
        # for each of the number tuples...
        for i in range(len(numTuples)):
            # get the first digit of that number.
            firstDigit = numTuples[i][0]
            
            # for each of the alternate nums after that one...
            for j in range(i+1, len(numTuples)):
                # get the last digit of the number.
                lastDigit = numTuples[j][-1]
                
                # if the digits have a gcd() of 1, increase the number of 
                # beautiful pairs.
                if gcd(firstDigit, lastDigit) == 1:
                    numBeautifulPairs += 1
                
        return numBeautifulPairs
        
    # This is a replacement for the standard gcd(), or Greatest Common Divisor 
    # function passed in two integers and returning the greatest divisor that 
    # divides them both.
    def gcd(self, a: int, b: int) -> int:
        # define the divisor that we're considering, starting from the smaller
        # of them.
        divisor = min(a, b)
        
        # while the divisor is greater than 0...
        while divisor > 0:
            # if both a and b can be divided by those, return the divisor.
            if (a % divisor == 0) and (b % divisor == 0):
                return divisor
            
            # decrement the divisor.
            divisor -= 1

        # it's gauranteed we will find something because both a and b will 
        # be divisible by 1 in the cases that we are using this. 
