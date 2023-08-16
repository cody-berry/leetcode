# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# define a cache, containing ns from 1 to 8.

# set the n at 1 to a list containing a tree node saying 1. 

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # if the cache at n is defined, return that.

        # call generateTrees at n-1. it will garuntee there's a cache element for every one below this one. 

        # define the result.

        # for each n from 1 to n (call it i)...

            # if i is n...

                # for each element of the result for n-1...
                    
                    # append a treenode containing n with a left of that element to result.
                
            # if i is 1...

                # for each element of the cache for n-1...

                    # do a depth-first search for each node and modify it to contain its nodes plus 1.

                    # append a treenode containing 1 with a right of that modified element to result.

            # if neither of those are the case...

                # for each element of the cache for i-1...

                    # for each element of the cache for n-i...

                        # do a depth-first search for each node of the element of the cache for n-i and modify
                        # it to contain its nodes plus i. 

                        # append a treenode containing i with a left of the element for i-1 and a right of the
                        # modified element for n-i.

        # return the result.
        return []
