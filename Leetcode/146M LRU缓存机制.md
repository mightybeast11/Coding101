# HashMap + DoublyLinkedList

Time: O(1)

```python
class DLNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.map = defaultdict()
        # initiate doubly linked list
        self.head = DLNode()
        self.tail = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.map.keys():
            return -1
        node = self.map[key]
        # update cache
        self.deleteExisting(node)
        self.addNew(node)
        return node.val

    def put(self, key, value):
        if key in self.map.keys():
            node = self.map[key]
            node.val = value
            self.deleteExisting(node)
            self.addNew(node)
        else:
            node = DLNode(key, value)
            self.map[key] = node
            self.addNew(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.deleteOld()
                self.map.pop(removed.key)
                self.size -= 1

    def addNew(self, node):
        # Add at list head.
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def deleteOld(self):
        # Remove from list tail, return the node.
        node = self.tail.prev
        self.deleteExisting(node)
        return node

    def deleteExisting(self, node):
        # Delete node from middle of the list.
        node.prev.next = node.next
        node.next.prev = node.prev
```

参考了官方题解: https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/

-   双向链表? 需要O(1)的时间access链表的两端. 单链表只能O(1)时间access head那一端, 做不到两端, 
-   哈希表的key就是`key`, value是双向链表中的node, 这样才能做到O(1)的时间access链表中的node.
-   为什么node要存key? 在删除尾部结点时, 如果node中没有key, 就无法从HashMap中删除这个node. `self.map.pop(removed.key)`



双向链表需要三个自定义操作:

1.  在head添加最新创建的结点

2.  在tail删除最不常用的结点

3.  将链表中间的结点提到head. (操作3 = 链表中间删除结点 + 操作1)

    因为上面两个操作本来就是O(1), 所以这个操作才是O(1)的关键. 为了实现O(1), 我们需要直接access中间的结点, 但是众所周知链表做不到这一点, 所以我们需要额外的HashMap来帮助实现. HashMap用key得到对应的结点, 然后我们从链表删除此结点, 并将其添加到头部 (也就是操作1).