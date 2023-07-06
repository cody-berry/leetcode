class Solution:
    # Taking in 2 integers num1 and num2, this function returns
    # the minimum number of operations requiredto make num1 0. 
    # In each operation, subtract 2ⁱ + num2 where i is any 
    # integer. num1 can only be positive, while num2 can be
    # negative.
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # if num1 is less than or equal to num2, then the first 
        # operation will reduce num1 to less than 0 which we
        # can't recover from.
        
        # otherwise...
            # start a BFS algorithm where each node is the 
            # number and each edge is a one-directional edge.
            
            # define the queue, which starts with num1.
            
            # define a visited list to make sure that we don't
            # run into an infinite loop. also trims so that if
            # two numbers can lead to one number, it isn't 
            # considered twice. starts with num1. 
            
            # define the round number, which is the number of
            # operations we've applied to the number.

            # while there is an element in the queue...
                
                # iterate through all of the elements in the 
                # queue that exist right now.

                    # dequeue the element at the beginning.

                    # subtract num2.

                    # if the number is negative and num2 is
                    # greater than -2, there is no way to bring
                    # it back up to 0.

                    # make an exit condition. while that exit
                    # condition is false...

                        # subtract 2^i. 

                        # if that minus num2 is greater than 0...
                        
                            # add that to the stack if the number
                            # isn't already visited.
                        
                        # otherwise...

                            # set the exit condition to true. 

                            # add i and i+1 to the stack as long
                            # as the resulting numbers aren't
                            # already visited and num2 is less
                            # than -1.

                        # increment i.
                        

            # if there is nothing left in the queue, we've
            # considered all reasonable possibilities and there's
            # no way to bring it to 0.
