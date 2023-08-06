class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # this is a "BFS algorithm" and it needs a queue. each entry is the number of 
        # characters visited, which starts at 0
        queue = [0]
        
        # define the number of iterations, which is the number of beautiful substrings
        numIterations = 0
        
        # while the queue isn't empty...
        while queue:
            # get the length of the queue
            lenQueue = len(queue)
            
            # get each element of the queue
            for i in range(lenQueue):
                # get the number of characters visited
                charactersVisited = queue.pop(0)
                
                # check each binary string. if the next few characters is that binary string,
                # append the entry to the queue. 
                restOfString = s[charactersVisited:]
                if (restOfString == ""):
                    return numIterations
                if (restOfString[0] == "1"):
                    queue.append(charactersVisited + 1)
                if (restOfString[:3] == "101"):
                    queue.append(charactersVisited + 3)
                if (restOfString[:5] == "11001"):
                    queue.append(charactersVisited + 5)
                if (restOfString[:7] == "1111101"):
                    queue.append(charactersVisited + 7)
                if (restOfString[:10] == "1001110001"):
                    queue.append(charactersVisited + 10)
                if (restOfString[:12] == "110000110101"):
                    queue.append(charactersVisited + 12)
                if (restOfString[:14] == "11110100001001"):
                    queue.append(charactersVisited + 14)
                
            # increment the number of iterations
            numIterations = numIterations + 1
            
        print("End of ", s)
        
        return -1
