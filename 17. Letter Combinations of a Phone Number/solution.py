# define the mapping of digits from 2-9 to a list of letters

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if digits is of length one, return the mapping of digits accessing the digit

        # if digits is of length zero, return an empty list

        # otherwise, get the mapping of digits accessing the last digit

        # define the result

        # then recursively call on this function except without the last digit

        # for each string inside...

            # for each of the map of digits accessing the last digit...

                # append the letter to the string, then append it to result.

        # return the result
