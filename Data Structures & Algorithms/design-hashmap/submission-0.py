class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i in range(self.size):
            pos = (idx + i) % self.size
            if self.table[pos] is None or self.table[pos] == (-1, -1):
                self.table[pos] = (key, value)
                return
            if self.table[pos][0] == key:       # key already exists → update
                self.table[pos] = (key, value)
                return

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for i in range(self.size):
            pos = (idx + i) % self.size
            if self.table[pos] is None:
                return -1
            if self.table[pos] == (-1, -1):
                continue
            if self.table[pos][0] == key:
                return self.table[pos][1]
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i in range(self.size):
            pos = (idx + i) % self.size
            if self.table[pos] is None:
                return
            if self.table[pos] == (-1, -1):
                continue
            if self.table[pos][0] == key:
                self.table[pos] = (-1, -1)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)