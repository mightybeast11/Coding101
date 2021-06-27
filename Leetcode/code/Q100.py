from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False 

        # BFS
        d1 = deque()
        d1.append(p)
        d2 = deque()
        d2.append(q)
        while d1 and d2:
            a, b = d1.popleft(), d2.popleft()
            if a.val != b.val: # check value
                return False
            # check left
            if bool(a.left) != bool(b.left): # xor
                return False
            if a.left != None:
                d1.append(a.left)
                d2.append(b.left)
            # check right
            if bool(a.right) != bool(b.right): # xor
                return False
            if a.right != None:
                d1.append(a.right)
                d2.append(b.right)

        return True

if __name__ == '__main__':
    sol = Solution()

    # test 1
    # t1 = []
    # print(sol.isSameTree(p, q))
    
    # # test 2
    # t2 = []
    # print(sol.isSameTree(p, q))
