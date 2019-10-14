# Question: Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
# Difficulty: Hard


class LRUCache:
    def __init__(self, capacity: int):
        self.hash = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        node = Node(key, value)
        self.add(node)
        self.hash[key] = node
        if len(self.hash) > self.cap:
            oldest = self.head.next
            self.remove(oldest)
            del self.hash[oldest.key]

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def add(self, node):
        beforeTail = self.tail.prev
        beforeTail.next = node
        self.tail.prev = node
        node.prev = beforeTail
        node.next = self.tail


class Node:
    def __init__(self, k, x, n=None, m=None):
        self.key = k
        self.val = x
        self.next = n
        self.prev = m
