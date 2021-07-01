class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
