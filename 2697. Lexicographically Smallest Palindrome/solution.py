class Solution:
    # Given a string, this function returns the lexicographically smallest palindrome made
    # by replacing the letters the least amount of times. a is lexicographically smaller 
    # than b if, in the first place where a and b differ, a's letter appears earlier in
    # the alphabet then the respective letter in b does.
    def makeSmallestPalindrome(self, s: str) -> str:
        # These are the two indices that, in the resulting string, we are going to make the same.
        # If the string length is odd, then the center should be the middle letter, and the first
        # and last indices surround it.
        if (len(s) % 2 == 1):
            firstIndex = floor(len(s)/2) - 1
            lastIndex = floor(len(s)/2) + 1
        
        # If the string length is even, then the first and last index should be the letters around
        # the middle.
        else:
            firstIndex = floor(len(s)/2) - 1
            lastIndex = floor(len(s)/2)
        
        # This is the resulting string.
        changedString = s
        
        # While the first index is in range of the string...
        while (firstIndex >= 0):
            # Check the letters in the index of the resulting string.
            if (s[firstIndex] != s[lastIndex]):
                # If they are different, then check the code of the letters. Note that this is
                # only lowercase English letters, so there will be no confusions.
                if (s[firstIndex] > s[lastIndex]):
                    smallestLetter = s[lastIndex]
                else:
                    smallestLetter = s[firstIndex]
                
                # Make the letter with the bigger code the one with the smaller code.
                changedString = (changedString[:firstIndex] + smallestLetter + 
                                changedString[(firstIndex+1):lastIndex] + 
                                smallestLetter + changedString[(lastIndex+1):])
            firstIndex -= 1
            lastIndex += 1
        
        # Return the resulting string.
        return changedString
