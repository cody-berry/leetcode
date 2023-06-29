class Solution:
    # Given a list of nums, it returns the number of beautiful pairs. A pair of
    # numbers is called "beautiful" if the greatest common divisor of the first
    # digit of the first number and the last digit of the second number have a 
    # greatest common divisor of 1, which is exactly what the second function 
    # handles.
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # define the number of beautiful pairs.
        
        # define an alternate nums list that's a tuple of the first and last
        # digits of the number.
        
        # for each of the alternate nums...
            
            # get the first digit of that number.
            
            # for each of the alternate nums after that one...
                
                # get the last digit of the number.
                
                # if the digits have a gcd() of 1, increase the number of 
                # beautiful pairs.
        
    # This is a replacement for the standard gcd(), or Greatest Common Divisor 
    # function passed in two integers and returning the greatest divisor that 
    # divides them both.
    def gcd(self, a: int, b: int) -> int:
        # define the divisor that we're considering, starting from the smaller
        # of them.
        
        # while the divisor is greater than 0...
        
            # if both a and b can be divided by those, return the divisor.
            
            # decrement the divisor.

        # there is a garuntee we will find something because both a and b will 
        # be divisible by 1 in the cases that we are using this. 
    
