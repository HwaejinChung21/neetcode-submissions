class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.least = Node(0, 0)
        self.most = Node(0, 0)
        self.least.next = self.most
        self.most.prev = self.least

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def insert(self, node) -> None:
        prev = self.most.prev
        nxt = self.most
        prev.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = prev

    def remove(self, node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]



        
