from typing import List, Dict

class Solution:
    def initializeBinaryLiftingTable(self, receiver: List[int], k: int):
        binaryLiftingTable = {}
        for i in range(len(receiver)):
            binaryLiftingTable[i] = {0: [receiver[i], i]}

        for i in range(1, k.bit_length()):
            for j in range(len(receiver)):
                binaryLiftingTable[j][i] = [
                    binaryLiftingTable[binaryLiftingTable[j][i-1][0]][i-1][0],
                    binaryLiftingTable[binaryLiftingTable[j][i-1][0]][i-1][1] + binaryLiftingTable[j][i-1][1]
                ]

        return binaryLiftingTable

        
    # given a passer-receiver list and a list of k's, this function 
    # returns the maximum value of a fucntion based on a ball-passing 
    # game. f(x, k) = x + f(receiver[x], k-1) if k > 0 and x if k = 0.
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        # initialize the binary lifting table.
        binaryLiftingTable = self.initializeBinaryLiftingTable(receiver, k)

        # record the binary representation of k
        powers = [(len(bin(k)) - 1 - i) for i, bit in enumerate(bin(k)) if bit == '1']

        # use f
        return max([self.ballPassSim(receiver, i, powers, binaryLiftingTable) for i in range(len(receiver))])
        
    def ballPassSim(self, receiver: List[int], x: int, powersOfK: int, binaryLiftingTable: Dict[int, Dict[int, List[int]]]) -> int:
        currentScore = 0
        ballPosition = x
        for power in powersOfK:
            newDataFromPower = binaryLiftingTable[ballPosition][power]
            currentScore += newDataFromPower[1]
            ballPosition = newDataFromPower[0]
        return currentScore + ballPosition
