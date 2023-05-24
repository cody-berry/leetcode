class Solution:
    # taken the number of players, n, and a constant, k, it returns the losers of a circular game. player 1 starts with the ball,
    # and passes it to the person k times away from him. The same thing for 2*k. Then 3*k. And so on until the player who has 
    # received the ball 2 times wins and the players who didn't receive the ball at all lose.
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # define an array of the people who will currently lose
        losers = []
        for i in range(n):
            losers.append(i + 1)
        print(losers)
        # which player holds the ball?
        ballHolder = 1
        # how many iterations have gone by? (it determines who gets the ball after each round)
        iterations = 0
        # simulate the game
        while True:
            # remove the current ballholder from the losers list. if the ballholder has already received the ball once, or is 
            # not a potential loser, we return all the losers. 
            ballHolderInLosers = False
            for loser in losers:
                if loser == ballHolder:
                    losers.remove(ballHolder)
                    ballHolderInLosers = True
                    break
            if not ballHolderInLosers:
                return losers
            # transfer the ball to another player. 
            ballHolder = ((ballHolder + iterations*k + k - 1) % n) + 1
            iterations = iterations + 1
