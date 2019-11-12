# LeetCode
# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
      self.cache = OrderedDict()
      self.capacity = capacity

    def get(self, key: int) -> int:
      value = self.cache.pop(key, None)
      if value is None:
        return -1
      
      self.cache[key] = value
      return value
    
    def put(self, key: int, value: int) -> None:
      if not self.cache.pop(key, None) and self.capacity == len(self.cache):
        self.cache.popitem(last=False)
      self.cache[key] = value
      
# For test
# obj = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1)) # returns 1
# cache.put(3, 3) # evicts key 2
# print(cache.get(2)) # returns -1 (not found)
# cache.put(4, 4) # evicts key 1
# print(cache.get(1)) # returns -1 (not found)
# print(cache.get(3)) # returns 3
# print(cache.get(4)) # returns 4
