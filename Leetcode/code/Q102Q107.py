from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    ret = [] # return value: list of list, each list inside is one level
    # edge case
    if root == None:
        return ret
    
    d = deque() # deque for BFS
    d.append(root)

    while d: # ensure all nodes are covered
        # each whhile loop covers one level
        level_length = len(d) # key idea of BFS
        level = []
        for _ in range(level_length):
            node = d.popleft()
            level.append(node.val)
            # expand next level
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        ret.append(level)
    
    print(ret)
    return ret # Q102
    # return list(reversed(ret)) # Q107


if __name__=='__main__':
    left = TreeNode(2, None, None)
    right = TreeNode(3, None, None)
    tree = TreeNode(1, left, right)
    levelOrderTraversal(tree) # [[1], [2, 3]]
