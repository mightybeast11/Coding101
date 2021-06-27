# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque
class Solution:
    def listOfDepth(self, tree):
        if tree == None:
            return []
        
        l = []
        d = deque()
        d.append(tree)
        while d:
            head = ListNode(-1) # need this head to add current linkedlist into return value
            cur = head
            for _ in range(len(d)):
                treeNode = d.popleft()
                listNode = ListNode(treeNode.val)
                cur.next = listNode
                cur = cur.next
                if treeNode.left != None:
                    d.append(treeNode.left)
                if treeNode.right != None:
                    d.append(treeNode.right)
            l.append(head.next)
        
        return l
