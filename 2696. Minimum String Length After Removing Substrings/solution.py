class Solution:
    # Given a string of uppercase letters, this function removes AB and CD strings as much
    # as possible and then returns the length of the string. note that removing an AB or
    # CD string might produce a new one.
    def minLength(self, s: str) -> int:
        # what is the index of the first character we are considering?

        # iterate until the index is 2 characters from the length of the string

            # if the pair of characters is AB or CD...

                # remove the characters...

                # and if this is not the first index...

                    # decrement the index so that next iteration, we consider whether
                    # it cleared the way for an AB or CD. 

            # otherwise...

                # if the next character is A or C...

                    # we can consider it...

                # and otherwise...

                    # skip it and advance twice.

        return 2
