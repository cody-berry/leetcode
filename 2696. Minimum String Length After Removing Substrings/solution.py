class Solution:
    # Given a string of uppercase letters, this function removes AB and CD strings as much
    # as possible and then returns the length of the string. note that removing an AB or
    # CD string might produce a new one.
    def minLength(self, s: str) -> int:
        # this is the index of the first character we are considering

        # iterate until the index is 2 characters from the length of the string

            # if the pair of characters is AB or CD...

                # remove the characters...

                # and if this is not the first index...

                    # decrement the index so that next iteration, we consider whether
                    # it cleared the way for an AB or CD. 

            # otherwise...

                # increment the index
        
        # return the length of the string
        return len(s)
