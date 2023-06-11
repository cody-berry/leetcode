class Solution:
    # Given a string of uppercase letters, this function removes AB and CD strings as much
    # as possible and then returns the length of the string. note that removing an AB or
    # CD string might produce a new one.
    # TODO: Replace this with multiple calls of replace()
    def minLength(self, s: str) -> int:
        # this is the index of the first character we are considering
        index = 0

        # iterate until the index is 2 characters from the length of the string
        while index < len(s) - 1:
            # if the pair of characters is AB or CD...
            if s[index:(index + 2)] in ["AB", "CD"]:
                # remove the characters... (assumes that this is the first instance)
                s = s.replace(s[index:(index + 2)], "", 1)

                # and if this is not the first index...
                if (index > 0):
                    # decrement the index so that next iteration, we consider whether
                    # it cleared the way for an AB or CD. 
                    index -= 1

            # otherwise, we prepare for the next iteration by incrementing the index.
            # IMPORTANT: Only do this if we didn't find a pair because otherwise the
            # two effects will cancel eachother out and patterns like ACDB will turn
            # into AB.
            else:
                # increment index.
                index += 1

        return len(s)
