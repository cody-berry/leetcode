class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # find the number of lets, rights, and underscores
        lefts = 0
        rights = 0
        underscores = 0
        for move in moves:
            if move == "L": lefts += 1
            if move == "R": rights += 1
            if move == "_": underscores += 1
        
        # return the result
        position = 0
        if rights > lefts:
            diff = rights - lefts
        if lefts > rights:
            diff = lefts - rights
        return diff + underscores
