class Solution:
    def addTwoNumbers(self, l1, l2):
        a = 0 # 记录当前位置的和, 并且记录进位, 每次循环结束只能是1或0
        head = ListNode(-1, None)
        cur = head
        while l1 != None or l2 != None or a != 0: # 2个数字或进位还没处理完
            if l1 != None:
                a += l1.val
                l1 = l1.next
            if l2 != None:
                a += l2.val
                l2 = l2.next
            cur.next = ListNode(a % 10, None)
            cur = cur.next
            a = 1 if a >= 10 else 0
        return head.next
