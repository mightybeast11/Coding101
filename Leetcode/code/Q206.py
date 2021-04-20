class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# head recursion
def  reverse_linkedlist(head):
    if head == None or head.next == None:
        return head
    ret = reverse_linkedlist(head.next) # the returned node
    head.next.next = head
    head.next = None # end case
    return ret

if __name__ == '__main__':
    n3 = Node(3, None)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    print(n1.next.next.value)
    print(reverse_linkedlist(n1).next.next.value)
