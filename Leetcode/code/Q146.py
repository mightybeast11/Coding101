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
