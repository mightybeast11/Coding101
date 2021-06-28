class Solution:
    def detectCycle(self, head):
        if head == None:
            return None

        slow, fast = head, head
        while fast != None: # fast will reach the end first if there is no ring
            slow = slow.next # slow.next can be None
            if fast.next != None: # fast.next cannot be None, need to call fast.next.next
                fast = fast.next.next
            else:
                return None # no ring
            if slow == fast: # 有环, 之后都不用检查next是否为None了
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer
        return None
